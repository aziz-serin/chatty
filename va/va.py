from flask import Flask
from openai_tools.config.config_manager import Config
from controllers.chat_controller import chat
from controllers.config_controller import config

app = Flask("chatty")

def init():
    app.config["system"] = Config("resources/config.ini", "system").entries
    app.config["mongo"] = Config("resources/config.ini", "flask").entries
    app.config["flask"] = Config("resources/config.ini", "mongo").entries

def register():
    app.register_blueprint(chat)
    app.register_blueprint(config)

def main():
    app.run(app.config["flask"]["host"], app.config["flask"]["port"])

if __name__ == "__main__":
    init()
    register()
    main()
