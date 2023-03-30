import openai
import logging
from .moderation import isValidPrompt
from .error import InvalidMessageError, TokenLimitError, NullResponseError, VAError
from .ai import OpenAI

logging.basicConfig(level = logging.DEBUG)

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
                 model: str = "gpt-3.5-turbo"):
        super().__init__(model)
        self.system_config = system_config
        self.config = config
        self.token_count=0
        self.__init_messages_with_config()
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

    def __handle_reason(self, reason:str):
        if reason == "stop":
            return
        elif reason == "length":
            raise TokenLimitError(f"{str(self.token_count)} is above the token limit for given model {self.model}")
        elif reason == "content_filter":
            raise InvalidMessageError("Invalid message was detected by chatgpt")
        elif reason == "null":
            raise NullResponseError()

    def send_message(self, message: str, conversation: bool) -> str:
        self.__validate_message(message)
        self.messages.append(
            {self.role: self.user, self.content: message}
        )
        response = self.__send_request()
        finish_reason = response['choices'][0]['finish_reason']
        self.token_count = int(response["usage"]["total_tokens"])
        self.__handle_reason(finish_reason)
        self.__log_transaction(str(response["created"]), finish_reason)
        reply = response['choices'][0]['message']['content']
        self.__handle_reply(reply, conversation)
        return reply

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
        logging.info(f'TIMESTAMP: {timestamp}, COUNT: {self.token_count}, RESPONSE_STATUS: {status}')
