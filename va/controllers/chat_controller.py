from flask import Blueprint, request, json, Response
from va.openai_tools.ai_chat import OpenAIChat
from . import factory, system_config
from va.openai_tools.error import InvalidMessageError, TokenLimitError, NullResponseError, VAError, OpenAIAPIKeyError

ai_chat = Blueprint('openai', "chatty")

@ai_chat.route("/chat", methods=['POST'])
def chat():
    content = request.get_json()
    prompt = content["prompt"]
    model = content["model"]
    token_limit = content["token_limit"]
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
        return Response(
            response=json.dumps({
                "reason": err.message
            }),
            status=400,
            mimetype='application/json'
        )
    except (OpenAIAPIKeyError | NullResponseError, VAError):
        return Response(
            response=json.dumps({
                "reason": "Internal Server Error"
            }),
            status=500,
            mimetype='application/json'
        )
