import gtts
import gtts.lang
from gtts import gTTS
from .error import UnsupportedLanguageError

class Talkie:
    supported_locales:dict

    def __init__(self, locale:str="en", slow:bool=False, lang_check:bool=False):
        self.locale = locale
        self.slow = slow
        self.lang_check = lang_check
        self.__init_supported_locales()
        self.__validate_given_language()

    def __init_supported_locales(self):
        self.supported_locales = gtts.lang.tts_langs()

    def __validate_given_language(self):
        if self.locale not in self.supported_locales.keys():
            raise UnsupportedLanguageError(f"Given language {self.locale} is not supported at the moment!")

    def save_sound(self, text:str, path:str):
        tts = gTTS(text=text, slow=self.slow, lang_check=self.lang_check)
        tts.save(path)

    def play_sound(self, text:str):
        pass
    # TODO implement play sound after implementing the app

