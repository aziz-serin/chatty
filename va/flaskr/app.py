from flask import Flask
from va.mongo.connection import Connection
from pymongo.errors import ConfigurationError, ConnectionFailure
from .error import AppConstructionError, ConnectionConstructionError
import logging

logger = logging.getLogger("chatty")

class App:

    def __init__(self, db_host:str, db_port:int):
        # create and configure the app and the db connections
        try:
            config_connection = Connection(db_host, db_port, "config")
            message_connection = Connection(db_host, db_port, "message")
            self.most_recent_id = 2
            self.connections = {
                0: config_connection,
                1: message_connection
            }
        except (ConfigurationError, ConnectionFailure) as err:
            logger.error(err)
            raise AppConstructionError(err)
        try:
            app = Flask(__name__)
            self.__app__ = app
        except OSError as err:  # thrown if the defined port is already is in use:
            logger.error(err)
            raise AppConstructionError(err)

    def create_connection(self, db_host:str, connection_name:str, db_port:int) -> Connection:
        try:
            connection = Connection(db_host, db_port, connection_name)
            self.most_recent_id += 1
            self.connections[self.most_recent_id] = connection
            return connection

        except (ConfigurationError, ConnectionFailure) as err:
            logger.error(err)
            raise ConnectionConstructionError(err)

    def remove_connection(self, connection_id:int) -> Connection | None:
        try:
            return self.connections.pop(connection_id)
        except KeyError as err:
            logger.debug(err)
            return None

    def add_config(self, key:str, value:str):
        self.__app__[key] = value
