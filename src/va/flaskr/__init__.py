from flask import Flask
from src.va.openai_tools.config.config_manager import Config
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

app = Flask("chatty")

def init():
    app.app_context()
    app.config["system"] = Config("resources/config.ini", "system").entries
    app.config["mongo"] = Config("resources/config.ini", "mongo").entries
    app.config["flask"] = Config("resources/config.ini", "flask").entries

def register():
    from src.va.controllers.chat_controller import ai_chat
    app.register_blueprint(ai_chat)
    from src.va.controllers.context_controller import context
    app.register_blueprint(context)