from flask import Blueprint,request, json, Response
from . import factory
from src.va.context.context import Context
from pymongo.errors import PyMongoError
from .error import InvalidKeyError
import logging

from ..openai_tools.ai_chat import OpenAIChat

context = Blueprint('context', "chatty")
logger = logging.getLogger("chatty")

@context.route("/context", methods=['POST', 'GET', 'PUT', 'DELETE'])
def context_endpoint():
    context_id = request.args.get("context_id", default=None, type=str)
    if request.method == 'POST':
        response = __handle_post()
    elif request.method == 'GET':
        response = __handle_get(context_id)
    elif request.method == 'PUT':
        response = __handle_put(context_id)
    else:
        response = __handle_delete(context_id)
    return response

def __handle_post() -> Response:
    content = request.get_json()
    messages = []
    default = "false"
    try:
        chat_model = content["chat_model"]
        config = content["config"]
        stt_model = content["stt_model"]
        token_limit = int(content["token_limit"])
    except KeyError as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )

    try:
        messages = content["messages"]
        validate_openai_keys(messages)
    except KeyError:
        pass
    except InvalidKeyError as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )

    try:
        default = content["default"]
    except KeyError:
        pass
    context_obj = Context(
        config=config,
        chat_model=chat_model,
        stt_model=stt_model,
        token_limit=token_limit,
        messages=messages,
        default=(default)
    )
    context_connection = factory.get_context_connection()
    try:
        context_id = context_connection.insert_document(context_obj.jsonify())
    except PyMongoError as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Internal Server Error"
            }),
            status=500,
            mimetype='application/json'
        )
    return Response(
        response=json.dumps({
            "context_id": str(context_id)
        }),
        status=201,
        mimetype='application/json'
    )

def __handle_get(context_id:str = None) -> Response:
    if context_id is None:
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    connection = factory.get_context_connection()
    context_retrieved = connection.get_document_by_id(context_id)
    if context_retrieved is None:
        logger.info(f"Resource context {context_id} not found")
        return Response(
            response=json.dumps({
                "reason": "Not Found"
            }),
            status=404,
            mimetype='application/json'
        )
    # Replace ObjectId object with String for json.dumps() method
    context_retrieved["_id"] = str(context_retrieved["_id"])
    return Response(
            response=json.dumps(
                context_retrieved
            ),
            status=200,
            mimetype='application/json'
        )

def __handle_put(context_id:str = None) -> Response:
    content = dict(request.get_json())
    if context_id is None:
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    try:
        validate_context_fields(list(content.keys()))
    except InvalidKeyError as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    if "messages" in content.keys():
        try:
            validate_openai_keys(content["messages"])
        except InvalidKeyError as err:
            logger.debug(err)
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )
    response = __handle_get(context_id)
    if response.status_code != 200:
        return response
    context_json = dict(response.json)
    del context_json["_id"]
    for key in content:
        context_json[key] = content[key]
    connection = factory.get_context_connection()
    connection.update_document(_id=context_id, update=context_json)
    return Response(
        response=json.dumps({}),
        status=204,
        mimetype='application/json'
    )

def __handle_delete(context_id:str = None) -> Response:
    if context_id is None:
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    connection = factory.get_context_connection()
    if connection.get_document_by_id(context_id) is not None:
        connection.delete_document(context_id)
        return Response(
            response={},
            status=204,
            mimetype='application/json'
        )
    else:
        logger.info(f"Resource context {context_id} not found")
        return Response(
            response=json.dumps({
                "reason": "Not Found"
            }),
            status=404,
            mimetype='application/json'
        )

def validate_openai_keys(messages:list[dict]):
    valid_keys = [OpenAIChat.role, OpenAIChat.content, OpenAIChat.system, OpenAIChat.user, OpenAIChat.assistant]
    for message in messages:
        check = all(item in valid_keys for item in list(message.keys()))
        if not check:
            raise InvalidKeyError("Some keys are not supported by openai APIs")

def validate_context_fields(key_list:list):
    context_fields = ["config", "chat_model", "stt_model", "token_limit", "messages", "default"]
    check = all(item in context_fields for item in key_list)
    if not check:
        raise InvalidKeyError("Some keys are not supported by context object")
