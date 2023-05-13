from src.va.mongo.connection_factory import ConnectionFactory
from src.va.flaskr import app
from flask import current_app

class Service:
    def __init__(self):
        with app.app_context():
            self.mongo_config = current_app.config["mongo"]
            self.system_config = current_app.config["system"]
            self.factory = ConnectionFactory(self.mongo_config["host"],
                                        int(self.mongo_config["port"]),
                                        self.mongo_config["username"],
                                        self.mongo_config["password"])