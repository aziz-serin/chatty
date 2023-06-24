from flask import Blueprint, request
from src.va.services.tts_service import TtsService

tts = Blueprint('tts', "chatty")
tts_service = TtsService()

@tts.route("/api/tts", methods=['POST'])
def tts_endpoint():
    return tts_service.tts(content=dict(request.get_json()))