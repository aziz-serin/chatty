from .error import UnsupportedLanguageError
from google.cloud import texttospeech as tts
import logging

class Talkie:
    supported_locales:set

    def __init__(self, voice_name:str="en-GB-Neural2-A"):
        self.client = tts.TextToSpeechClient()
        self.logger = logging.getLogger("chatty")
        self.supported_locales = self.__get_languages__()
        locale = "-".join(voice_name.split("-")[:2])
        self.__validate_locale__(locale)
        self.voice_params = tts.VoiceSelectionParams(
            language_code=locale, name=voice_name
        )
        self.audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    def __validate_locale__(self, locale:str):
        if locale not in self.supported_locales:
            message = f"Given locale {locale} is not supported by Google text to speech API!"
            self.logger.error(message)
            raise UnsupportedLanguageError(message)

    def __get_languages__(self) -> set:
        voices = self.client.list_voices().voices
        languages = set()
        for voice in voices:
            for language_code in voice.language_codes:
                languages.add(language_code)
        return languages

    def get_sound(self, text:str) -> bytes | None:
        text_input = tts.SynthesisInput(text=text)

        response = self.client.synthesize_speech(
            input=text_input,
            voice=self.voice_params,
            audio_config=self.audio_config
        )
        return response.audio_content

    def save_sound(self, file:bytes, filename:str) -> bool:
        try:
            with open(filename, "wb") as out:
                out.write(file)
                self.logger.info(f'Generated speech file and saved it to {filename}')
                return True
        except IOError as err:
            self.logger.error(err)
            return False