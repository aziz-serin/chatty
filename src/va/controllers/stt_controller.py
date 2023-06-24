from flask import Blueprint, request, Response, json
from src.va.services.stt_service import SttService
from werkzeug.utils import secure_filename
import logging

stt = Blueprint('speech_to_text', "chatty")
stt_service = SttService()
logger = logging.getLogger("chatty")

@stt.route("/api/stt", methods=['POST'])
def stt_endpoint() -> Response:
    if 'file' not in request.files:
        logger.debug("No file specified in the request")
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        logger.debug("Cannot process an empty file")
        return Response(
            response=json.dumps({
                "reason": "Invalid/Bad Request"
            }),
            status=400,
            mimetype='application/json'
        )
    if file and stt_service.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        method = request.args.get("method", default=stt_service.TRANSCRIBE, type=str)
        return stt_service.stt(filename, file, dict(request.form), method)

    logger.debug("Invalid file type/name")
    return Response(
        response=json.dumps({
            "reason": "Invalid/Bad Request"
        }),
        status=400,
        mimetype='application/json'
    )
