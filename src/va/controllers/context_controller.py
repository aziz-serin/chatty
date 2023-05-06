from flask import Blueprint,request, json, Response
from . import factory
import logging

context = Blueprint('context', "chatty")
logger = logging.getLogger("chatty")

@context.route("/context", methods=['POST', 'GET', 'PUT', 'DELETE'])
def context_endpoint():
    context_id = request.args.get("context_id", default=None, type=str)
    if request.method == 'POST':
        response = __handle_post()
    elif request.method == 'GET':
        response = __handle_get(context_id)
    elif request.method == 'PUT':
        response = __handle_put()
    else:
        response = __handle_delete(context_id)
    return response
def __handle_post() -> Response:
    pass

def __handle_get(context_id:str = None) -> Response:
    if context_id is None:
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    connection = factory.get_context_connection()
    context_retrieved = connection.get_document_by_id(context_id)
    if context_retrieved is None:
        logger.info(f"Resource context {context_id} not found")
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

def __handle_put() -> Response:
    pass

def __handle_delete(context_id:str = None) -> Response:
    if context_id is None:
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    connection = factory.get_context_connection()
    if connection.get_document_by_id(context_id) is not None:
        connection.delete_document(context_id)
        return Response(
            response={},
            status=204,
            mimetype='application/json'
        )
    else:
        logger.info(f"Resource context {context_id} not found")
        return Response(
            response=json.dumps({
                "reason": "Not Found"
            }),
            status=404,
            mimetype='application/json'
        )

