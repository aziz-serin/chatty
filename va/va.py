from flask import Flask
from openai_tools.config.config_manager import Config
from controllers.chat_controller import chat
from controllers.config_controller import config

app = Flask("chatty")

def init():
    openai_config = Config("resources/config.ini", "system")
    flask_config = Config("resources/config.ini", "flask")
    mongo_config = Config("resources/config.ini", "mongo")
    app.config["system"] = openai_config.entries
    app.config["mongo"] = mongo_config.entries
    app.config["flask"] = flask_config.entries

def register():
    app.register_blueprint(chat)
    app.register_blueprint(config)

def main():
    app.run(app.config["flask"]["host"], app.config["flask"]["port"])

if __name__ == "__main__":
    init()
    register()

