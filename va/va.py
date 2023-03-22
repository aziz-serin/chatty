import logging
from config.config_manager import Config
from configparser import NoSectionError

logging.basicConfig(level = logging.DEBUG)

def main():
    config = get_config("resources/config.ini")

def get_config(path:str) -> Config:
    config = Config(path)
    try:
        config.load_config()
    except NoSectionError as err:
        logging.debug(err)
        quit()
    return config

if __name__ == "__main__":
    main()
