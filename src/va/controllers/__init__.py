from src.va.mongo.connection_factory import ConnectionFactory
from src.va.flaskr import app
from flask import current_app

with app.app_context():
    mongo_config = current_app.config["mongo"]
    system_config = current_app.config["system"]

    factory = ConnectionFactory(mongo_config["host"],
                                int(mongo_config["port"]),
                                mongo_config["username"],
                                mongo_config["password"])
