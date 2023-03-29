from .error import UnsupportedLanguageError
from google.cloud import texttospeech as tts
from google.cloud.texttospeech import SsmlVoiceGender
import logging

logging.basicConfig(level = logging.DEBUG)

class Talkie:
    supported_locales:set

    def __init__(self, ssml_gender:SsmlVoiceGender=SsmlVoiceGender.NEUTRAL, locale:str="en-GB"):
        self.client = tts.TextToSpeechClient()
        self.gender = ssml_gender
        self.supported_locales = self.__get_languages__()
        self.__validate_locale(locale)
        self.locale = locale

    def __validate_locale(self, locale:str):
        if locale not in self.supported_locales:
            raise UnsupportedLanguageError(f"Given locale {locale} is not supported by Google text to speech API!")

    def __get_languages__(self) -> set:
        voices = self.client.list_voices().voices
        languages = set()
        for voice in voices:
            for language_code in voice.language_codes:
                languages.add(language_code)
        return languages

    def save_sound(self, text:str, filename:str):
        text_input = tts.SynthesisInput(text=text)
        voice_params = tts.VoiceSelectionParams(
            language_code = self.locale, ssml_gender=self.gender
        )
        audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)
        response = self.client.synthesize_speech(
            input=text_input,
            voice=voice_params,
            audio_config=audio_config
        )
        with open(filename, "wb") as out:
            out.write(response.audio_content)
            logging.info(f'Generated speech file and saved it to {filename}')