import pymongo

class DB:
    def __init__(self, db_host:str, db_port:int, username:str, password:str):
        self._client = pymongo.MongoClient(host=db_host, port=db_port, username=username, password=password)

    def get_database(self, db:str):
        return self._client[db]

    def get_databases(self) -> list:
        return self._client.list_database_names()

    def database_exists(self, db:str) -> bool:
        return db in self._client.list_database_names()

    def delete_database(self, db:str):
            self._client.drop_database(name_or_database=db)
