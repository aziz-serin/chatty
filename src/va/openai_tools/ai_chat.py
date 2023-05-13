import openai
import logging
from .moderation import isValidPrompt
from .error import InvalidMessageError, TokenLimitError, NullResponseError, VAError
from .ai import OpenAI
from .util import get_token_count

logger = logging.getLogger("chatty")

class OpenAIChat(OpenAI):
    """
    Default dict keys for openai at the time of writing this code
    """
    role:str = "role"
    content:str = "content"
    system:str = "system"
    user:str = "user"
    assistant:str = "assistant"

    def __init__(self, config: dict, system_config: str = "You are a virtual assistant.",
                 model: str = "gpt-3.5-turbo", token_limit:int = 4000, initial_messages:list[dict]=None):
        super().__init__(model)
        self.token_limit = token_limit
        self.system_config = system_config
        self.config = config
        if initial_messages is None:
            self.__init_messages_with_config()
        else:
            self.messages = initial_messages
        self.initial_messages = self.messages

    def __init_messages_with_config(self):
        self.messages = []
        system_message = self.system_config
        for key, value in self.config.items():
            message = f' {key}={value}'
            system_message = system_message + message
        self.messages.append(
            {self.role: self.system, self.content: system_message}
        )

    def __validate_message(self, message:str):
        response = isValidPrompt(message)
        if response["flagged"]:
            reasons = ', '.join(map(str, response["reasons"]))
            raise InvalidMessageError(reasons)

    def __validate_token_count(self):
        if self.get_current_token_count() >= self.token_limit:
            raise TokenLimitError(f"{self.get_current_token_count()} is above the token limit for given model {self.model}")

    def __handle_reason(self, reason:str):
        if reason == "stop":
            return
        elif reason == "length":
            raise TokenLimitError(f"{self.get_current_token_count()} is above the token limit for given model {self.model}")
        elif reason == "content_filter":
            raise InvalidMessageError("Invalid message was detected by chatgpt")
        elif reason == "null":
            raise NullResponseError()

    def send_message(self, message: str, conversation: bool) -> str:
        self.__validate_message(message)
        self.messages.append(
            {self.role: self.user, self.content: message}
        )
        self.__validate_token_count()
        response = self.__send_request()
        finish_reason = response['choices'][0]['finish_reason']
        self.__handle_reason(finish_reason)
        self.__log_transaction(str(response["created"]), finish_reason)
        reply = response['choices'][0]['message']['content']
        self.__handle_reply(reply, conversation)
        return reply

    """
    If conversation, leave the reply as None since the messages will contain the reply, if not, include the reply
    when asking for the token count
    """
    def get_current_token_count(self, reply:str = None):
        messages = self.messages
        if reply is not None:
            messages.append(
                {self.role: self.assistant, self.content: reply}
            )
        return get_token_count(messages, self.model)

    def __send_request(self):
        try:
            return openai.ChatCompletion.create(model=self.model, messages=self.messages)
        except openai.OpenAIError as err:
            logging.error(err.json_body)
            raise VAError(err.json_body)

    """
    Cache the response and the sent prompt if the interaction is a conversation.
    """
    def __handle_reply(self, reply: str, conversation:bool):
        if conversation:
            self.messages.append(
                {self.role: self.assistant, self.content: reply}
            )
        else:
            # Roll back the messages into the initial stage with only the config message
            self.messages = self.initial_messages

    def __log_transaction(self, timestamp: str, status: str):
        logger.info(f'TIMESTAMP: {timestamp}, COUNT: {self.get_current_token_count()}, RESPONSE_STATUS: {status}')
