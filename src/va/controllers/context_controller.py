from flask import Blueprint,request, json, Response
from . import factory
from src.va.context.context import Context
from pymongo.errors import PyMongoError
import logging

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
        response = __handle_put()
    else:
        response = __handle_delete(context_id)
    return response

#TODO implement validate messages function (mainly for the key validation so openai api is happy)

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
    except KeyError:
        pass

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

def __handle_put() -> Response:
    pass

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

