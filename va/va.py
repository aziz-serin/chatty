import logging
from openai_tools.config.config_manager import Config
from openai_tools.ai import OpenAI
from openai_tools.error import InvalidMessageError, TokenLimitError, NullResponseError
from configparser import NoSectionError

logging.basicConfig(level = logging.DEBUG)

def main():
    config = get_config("resources/config.ini", "personal_information")
    reply = get_singular_response("Message goes here", config)
    print(reply)

def get_config(path:str, section:str) -> Config:
    try:
        return Config(path, section)
    except NoSectionError:
        quit()

def get_singular_response(message:str, config:Config):
    ai = OpenAI(config=config)
    try:
        return ai.send_message(message=message, conversation=False)
    except (InvalidMessageError, TokenLimitError, NullResponseError) as err:
        logging.error(err.message)
        quit()

if __name__ == "__main__":
    main()
