import json

class Context:

    def __init__(self, config:dict, chat_model:str, stt_model:str, token_limit:int, messages:list[dict]):
        self.config = config
        self.chat_model = chat_model
        self.stt_model = stt_model
        self.token_limit = token_limit
        self.messages = messages

    def jsonify(self) -> json:
        json_obj = {
            "config": self.config,
            "chat_model": self.chat_model,
            "stt_model": self.stt_model,
            "token_limit": self.token_limit,
            "messages": self.messages
        }
        return json.dump(json_obj)

    def load_from_json(self, obj:json):
        self.config = obj["config"]
        self.chat_model = obj["chat_model"]
        self.stt_model = obj["stt_model"]
        self.token_limit = obj["token_limit"]
        self.messages = ["messages"]