import logging
from openai_tools.config.config_manager import Config
from openai_tools.ai_chat import OpenAIChat
from openai_tools.ai_audio import OpenAIAudio
from openai_tools.error import InvalidMessageError, TokenLimitError, NullResponseError, FileSizeError, VAError
from configparser import NoSectionError

logging.basicConfig(level = logging.DEBUG)

def main():
    config = get_config("resources/config.ini", "personal_information")
    reply = speech_to_text("resources/audio_sample.m4a")
    print(reply)

def get_config(path:str, section:str) -> Config:
    try:
        return Config(path, section)
    except NoSectionError:
        quit(1)

def get_singular_response(message:str, config:Config):
    ai = OpenAIChat(config=config)
    try:
        return ai.send_message(message=message, conversation=False)
    except (InvalidMessageError, TokenLimitError, NullResponseError) as err:
        logging.error(err.message)
        quit(1)
    except VAError:
        quit(1)

def speech_to_text(file_path:str):
    ai = OpenAIAudio()
    try:
        return ai.speech_to_text(file=file_path)
    except FileSizeError as err:
        logging.error(err.message)
        quit(1)
    except VAError:
        quit(1)

if __name__ == "__main__":
    main()
