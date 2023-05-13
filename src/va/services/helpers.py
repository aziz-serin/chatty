from src.va.openai_tools.ai_chat import OpenAIChat
from src.va.services.error import InvalidKeyError

def validate_openai_message_keys(messages:list[dict]):
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
