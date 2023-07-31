from io import BytesIO
from .service import Service
from flask import Response, json, send_file
from src.va.tts.talk import Talkie
from src.va.tts.error import UnsupportedLanguageError
import logging

class TtsService(Service):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("chatty")

    def tts(self, content:dict) -> Response:
        try:
            voice_name = content["voice_name"]
        except KeyError:
            voice_name = None
            # voice_name is an optional one
            pass

        try:
            text = content["text"]
        except KeyError:
            self.logger.debug("Text cannot be empty for tts request")
            return Response(
                response=json.dumps({
                    "reason": "Invalid/Bad Request"
                }),
                status=400,
                mimetype='application/json'
            )

        if voice_name is None:
            talkie = Talkie()
        else:
            try:
                talkie = Talkie(voice_name)
            except UnsupportedLanguageError as err:
                self.logger.error(err)
                return Response(
                    response=json.dumps({
                        "reason": "Invalid/Bad Request"
                    }),
                    status=400,
                    mimetype='application/json'
                )
        bytez = talkie.get_sound(text)
        return send_file(
            BytesIO(bytez),
            mimetype='audio/m4a',
            download_name='audio.m4a',
        )