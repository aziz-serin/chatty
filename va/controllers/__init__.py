from va.mongo.connection_factory import ConnectionFactory
import flask

mongo_host = flask.current_app.config["mongo"]["host"]
mongo_port = flask.current_app.config["mongo"]["port"]

factory = ConnectionFactory(mongo_host, mongo_port)