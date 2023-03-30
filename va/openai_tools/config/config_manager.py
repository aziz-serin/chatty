import configparser
from configparser import NoSectionError
import logging

logger = logging.getLogger("chatty")

"""
Has the following instance variables:
    - cnf for configparser instance
    - entries is a dict which contains the given config
    - path for config file path
    - section for the name of the section
"""
class Config:
    def __init__(self, path:str, section:str):
        self.cnf = configparser.ConfigParser()
        self.path = path
        self.section = section
        self.cnf.read(path)
        if self.__file_empty():
            raise NoSectionError(section)
        self.cnf.options(section)
        self.entries = dict(self.cnf.items(section))

    """
    Use this to check if config input is needed when the app is launched for the first time 
    """
    def __file_empty(self) -> bool:
        if (not self.cnf.has_section(self.section)) or len(self.cnf.items()) == 0:
            logger.debug(f"Config is either empty or missing the given section {self.section}")
            return True
        return False

    def save_config(self):
        config_parser = configparser.ConfigParser()
        config_parser.add_section(self.section)
        for key, value in self.entries.items():
            config_parser.set(self.section, key, value)
        with open(self.path, "w") as f:
            config_parser.write(f)
