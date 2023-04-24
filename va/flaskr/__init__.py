from flask import Flask
from va.openai_tools.config.config_manager import Config

app = Flask("chatty")

def init():
    app.app_context()
    app.config["system"] = Config("resources/config.ini", "system").entries
    app.config["mongo"] = Config("resources/config.ini", "mongo").entries
    app.config["flask"] = Config("resources/config.ini", "flask").entries

def register():
    from va.controllers.chat_controller import ai_chat
    app.register_blueprint(ai_chat)
    from va.controllers.config_controller import config
    app.register_blueprint(config)