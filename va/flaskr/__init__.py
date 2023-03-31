from flask import Flask
from va.mongo.connection import Connection
from pymongo.errors import ConfigurationError, ConnectionFailure
import logging

config_connection = None
message_connection = None

logger = logging.getLogger("chatty")

def create_app(db_host:str, db_port:int) -> Flask | None:
    # create and configure the app and the db connections
    global config_connection
    global message_connection
    try:
        config_connection = Connection(db_host, db_port, "config")
        message_connection = Connection(db_host, db_port, "message")
    except (ConfigurationError, ConnectionFailure) as err:
        logger.error(err)
        return None
    try:
        app = Flask(__name__)
        return app
    except OSError as err: # thrown if the defined port is already is in use:
        logger.error(err)
        return None
