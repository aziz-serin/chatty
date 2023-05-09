# TODO implement a cache for context at app startup as it will be read a lot
class Context:
    def __init__(self, config:dict = None, chat_model:str = None, stt_model:str = None, token_limit:int = None,
                 messages:list[dict] = None, default:bool = False):
        self.config = config
        self.chat_model = chat_model
        self.stt_model = stt_model
        self.token_limit = token_limit
        self.messages = messages
        self.default = default

    def jsonify(self) -> dict:
        return {
            "config": self.config,
            "chat_model": self.chat_model,
            "stt_model": self.stt_model,
            "token_limit": self.token_limit,
            "messages": self.messages,
            "default": self.default,
        }

    def load_from_json(self, obj:dict) -> None:
        self.config = obj["config"]
        self.chat_model = obj["chat_model"]
        self.stt_model = obj["stt_model"]
        self.token_limit = obj["token_limit"]
        self.messages = obj["messages"]
        self.default = obj["default"]
