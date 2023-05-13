from flask import json, Response
from src.va.context.context import Context
from pymongo.errors import PyMongoError
from .error import InvalidKeyError
from .service import Service
import logging

class ContextService(Service):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("chatty")

    def create_context(self, content:dict) -> Response:
        messages = []
        default = "false"
        try:
            chat_model = content["chat_model"]
            config = content["config"]
            stt_model = content["stt_model"]
            token_limit = int(content["token_limit"])
        except KeyError as err:
            self.logger.debug(err)
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )

        try:
            messages = content["messages"]
            self.validate_openai_message_keys(messages)
        except KeyError:
            pass
        except InvalidKeyError as err:
            self.logger.debug(err)
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )
        try:
            default = content["default"]
        except KeyError:
            pass
        context_obj = Context(
            config=config,
            chat_model=chat_model,
            stt_model=stt_model,
            token_limit=token_limit,
            messages=messages,
            default=default
        )
        context_connection = self.factory.get_context_connection()
        try:
            context_id = context_connection.insert_document(context_obj.jsonify())
        except PyMongoError as err:
            self.logger.debug(err)
            return Response(
                response=json.dumps({
                    "reason": "Internal Server Error"
                }),
                status=500,
                mimetype='application/json'
            )
        return Response(
            response=json.dumps({
                "context_id": str(context_id)
            }),
            status=201,
            mimetype='application/json'
        )

    def get_context(self, context_id: str = None) -> Response:
        if context_id is None:
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )
        connection = self.factory.get_context_connection()
        context_retrieved = connection.get_document_by_id(context_id)
        if context_retrieved is None:
            self.logger.info(f"Resource context {context_id} not found")
            return Response(
                response=json.dumps({
                    "reason": "Not Found"
                }),
                status=404,
                mimetype='application/json'
            )
        # Replace ObjectId object with String for json.dumps() method
        context_retrieved["_id"] = str(context_retrieved["_id"])
        return Response(
            response=json.dumps(
                context_retrieved
            ),
            status=200,
            mimetype='application/json'
        )

    def edit_context(self, content:dict, context_id: str = None) -> Response:
        if context_id is None:
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )
        try:
            self.validate_context_fields(list(content.keys()))
        except InvalidKeyError as err:
            self.logger.debug(err)
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )
        if "messages" in content.keys():
            try:
                self.validate_openai_message_keys(content["messages"])
            except InvalidKeyError as err:
                self.logger.debug(err)
                return Response(
                    response=json.dumps({
                        "reason": "Invalid/Bad Request"
                    }),
                    status=400,
                    mimetype='application/json'
                )
        response = self.get_context(context_id)
        if response.status_code != 200:
            return response
        context_json = dict(response.json)
        del context_json["_id"]
        for key in content:
            context_json[key] = content[key]
        connection = self.factory.get_context_connection()
        connection.update_document(_id=context_id, update=context_json)
        return Response(
            response=json.dumps({}),
            status=204,
            mimetype='application/json'
        )

    def delete_context(self, context_id: str = None) -> Response:
        if context_id is None:
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )
        connection = self.factory.get_context_connection()
        if connection.get_document_by_id(context_id) is not None:
            connection.delete_document(context_id)
            return Response(
                response={},
                status=204,
                mimetype='application/json'
            )
        else:
            self.logger.info(f"Resource context {context_id} not found")
            return Response(
                response=json.dumps({
                    "reason": "Not Found"
                }),
                status=404,
                mimetype='application/json'
            )

    def get_all_contexts(self):
        context_connection = self.factory.get_context_connection()
        contexts = context_connection.get_all_documents()
        return Response(
            response=json.dumps(contexts),
            status=200,
            mimetype='application/json'
        )
