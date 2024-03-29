from flask import Flask
from src.va.openai_tools.config.config_manager import Config
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

app = Flask("chatty")

def init():
    app.app_context()
    resources_path = "src/va/resources"
    app.config["system"] = Config(f"{resources_path}/config.ini", "system").entries
    app.config["mongo"] = Config(f"{resources_path}/config.ini", "mongo").entries
    app.config["flask"] = Config(f"{resources_path}/config.ini", "flask").entries
    app.config["MAX_CONTENT_PATH"] = 26_214_400
    app.config["UPLOAD_FOLDER"] = resources_path
    app.config["ORIGINS"] = Config(f"{resources_path}/config.ini", "origins").entries
    __setup_cors__()

def __setup_cors__():
    CORS(app, origins=[app.config["ORIGINS"]["origin"]])

def __registerApi__():
    from src.va.controllers.chat_controller import ai_chat
    app.register_blueprint(ai_chat)
    from src.va.controllers.context_controller import context
    app.register_blueprint(context)
    from src.va.controllers.stt_controller import stt
    app.register_blueprint(stt)
    from src.va.controllers.tts_controller import tts
    app.register_blueprint(tts)

def registerBlueprint():
    logger = logging.getLogger("chatty")
    __registerApi__()
    logger.debug("Registered API endpoints")