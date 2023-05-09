from flask import Blueprint, request, json, Response
from src.va.openai_tools.ai_chat import OpenAIChat
from src.va.context.context import Context
from . import system_config, factory
import logging
from src.va.openai_tools.error import InvalidMessageError, TokenLimitError, NullResponseError, VAError, OpenAIAPIKeyError

ai_chat = Blueprint('openai', "chatty")

logger = logging.getLogger("chatty")

chat_default_context = Context(
    config={},
    chat_model="gpt-3.5-turbo",
    token_limit= 4000,
    default=True
)

@ai_chat.route("/chat", methods=['POST'])
def chat() -> Response:
    content = request.get_json()
    try:
        prompt = content["prompt"]
        model = content["model"]
        token_limit = content["token_limit"]
    except KeyError as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    openai_chat = OpenAIChat(
        model=model,
        config=system_config,
        token_limit=token_limit
    )
    try:
        system = content["system_config"]
        openai_chat.system_config = system
    except KeyError:
        pass
    try:
        response = openai_chat.send_message(prompt, False)
        data = {
            "response": response,
            "token_count": openai_chat.get_current_token_count()
        }
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except (InvalidMessageError | TokenLimitError) as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    except (OpenAIAPIKeyError | NullResponseError, VAError) as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Internal Server Error"
            }),
            status=500,
            mimetype='application/json'
        )

@ai_chat.route("/conversation", methods=['POST'])
def conversation() -> Response:
    connection = factory.get_context_connection()
    if connection is None:
        logger.debug("Could not establish connection with database")
        return Response(
            response=json.dumps({
                "reason": "Internal Server Error"
            }),
            status=500,
            mimetype='application/json'
        )
    content = request.get_json()
    try:
        prompt = content["prompt"]
    except KeyError as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    context_id = None
    try:
        context_id = content["context_id"]
    except KeyError:
        pass

    if context_id is not None:
        context_document = connection.get_document_by_id(context_id)
        if context_document is not None:
            context = Context()
            context.load_from_json(context_document)
        else:
            context = chat_default_context
    else:
        context = chat_default_context

    openai_chat = OpenAIChat(
        model=context.chat_model,
        config=context.config,
        token_limit=context.token_limit,
        initial_messages=context.messages
    )
    try:
        system = content["system_config"]
        openai_chat.system_config = system
    except KeyError:
        pass
    try:
        response = openai_chat.send_message(prompt, True)
        context.messages = openai_chat.messages
        if context.default:
            # We are writing it, not default anymore
            context.default = False
            context_id = connection.insert_document(context.jsonify())
        else:
            connection.update_document(context_id, context.jsonify())
        data = {
            "response": response,
            "token_count": openai_chat.get_current_token_count(),
            "context_id": str(context_id)
        }
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except (InvalidMessageError | TokenLimitError) as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    except (OpenAIAPIKeyError | NullResponseError, VAError) as err:
        logger.debug(err)
        return Response(
            response=json.dumps({
                "reason": "Internal Server Error"
            }),
            status=500,
            mimetype='application/json'
        )
