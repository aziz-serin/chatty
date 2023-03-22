import configparser

class Config:
    path:str
    entries:dict

    def __init__(self, path:str):
        self.path = path
        self.entries = {}

    def load_config(self):
        cnf = configparser.ConfigParser()
        cnf.read("resources/config.ini")
        cnf.options('personal_information')
        self.entries = dict(cnf.items('personal_information'))

    """
    Use this to check if config input is needed when the app is launched for the first time 
    """
    def __file_empty(self) -> bool:
        return True if len(self.entries.keys()) == 0 else False

    def update_config(self, key:str, value):
        pass

    def get_entries(self):
        return self.entries

