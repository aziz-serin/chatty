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
    app.config["MAX_CONTENT_PATH"] = 26_214_400
    app.config["UPLOAD_FOLDER"] = "resources"

def register():
    from src.va.controllers.chat_controller import ai_chat
    app.register_blueprint(ai_chat)
    from src.va.controllers.context_controller import context
    app.register_blueprint(context)
    from src.va.controllers.stt_controller import stt
    app.register_blueprint(stt)
    from src.va.controllers.tts_controller import tts
    app.register_blueprint(tts)