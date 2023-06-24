from flask import Blueprint, request
from src.va.services.context_service import ContextService

context = Blueprint('context', "chatty")
context_service = ContextService()

@context.route("/api/context", methods=['POST', 'GET', 'PUT', 'DELETE'])
def context_endpoint():
    context_id = request.args.get("context_id", default=None, type=str)
    _all = context_service.str2bool(request.args.get("isAll", default=None, type=str))
    if request.method == 'POST':
        response = context_service.create_context(dict(request.get_json()))
    elif request.method == 'GET':
        if not _all:
            response = context_service.get_context(context_id)
        else:
            response = context_service.get_all_contexts()
    elif request.method == 'PUT':
        response = context_service.edit_context(context_id=context_id, content=dict(request.get_json()))
    else:
        response = context_service.delete_context(context_id)
    return response