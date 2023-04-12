from .error import UnsupportedLanguageError
from google.cloud import texttospeech as tts
import logging

logger = logging.getLogger("chatty")

class Talkie:
    supported_locales:set

    def __init__(self, voice_name:str="en-GB-Neural2-A"):
        self.client = tts.TextToSpeechClient()
        self.supported_locales = self.__get_languages__()
        locale = "-".join(voice_name.split("-")[:2])
        self.__validate_locale(locale)
        self.voice_params = tts.VoiceSelectionParams(
            language_code=locale, name=voice_name
        )
        self.audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    def __validate_locale(self, locale:str):
        if locale not in self.supported_locales:
            message = f"Given locale {locale} is not supported by Google text to speech API!"
            logger.error(message)
            raise UnsupportedLanguageError(message)

    def __get_languages__(self) -> set:
        voices = self.client.list_voices().voices
        languages = set()
        for voice in voices:
            for language_code in voice.language_codes:
                languages.add(language_code)
        return languages

    def save_sound(self, text:str, filename:str):
        text_input = tts.SynthesisInput(text=text)

        response = self.client.synthesize_speech(
            input=text_input,
            voice=self.voice_params,
            audio_config=self.audio_config
        )
        with open(filename, "wb") as out:
            out.write(response.audio_content)
            logger.info(f'Generated speech file and saved it to {filename}')
