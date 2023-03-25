import logging
from config.config_manager import Config
from configparser import NoSectionError

logging.basicConfig(level = logging.DEBUG)

def main():
    config = get_config("resources/config.ini", "personal_information")
    entries = config.entries
    print(entries)

def get_config(path:str, section:str) -> Config:
    try:
        return Config(path, section)
    except NoSectionError:
        quit()

if __name__ == "__main__":
    main()
