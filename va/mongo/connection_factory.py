from connection import Connection
import logging
from pymongo.errors import PyMongoError

logger = logging.getLogger("chatty")

class ConnectionFactory:
    def __init__(self, db_host:str, db_port:int, username:str, password:str):
        self.db_host = db_host
        self.db_port = db_port
        self.username = username
        self.password = password

    def get_config_connection(self) -> Connection | None:
        return self.get_custom_connection("config")

    def get_message_connection(self) -> Connection | None:
        return self.get_custom_connection("message")

    def get_context_connection(self) -> Connection | None:
        return self.get_custom_connection("context")

    def get_custom_connection(self, connection:str) -> Connection | None:
        try:
            return Connection(self.db_host, self.db_port, connection, self.username, self.password)
        except PyMongoError as err:
            logger.error(err)
            return None
