from typing import Any
from .db import DB
import logging
from bson.objectid import ObjectId

logger = logging.getLogger("chatty")

class Connection:

    def __init__(self, db_host:str, port:int, collection_name:str, username:str, password:str):
        self.__client__ = DB(db_host, port, username, password)
        self.collection_name = collection_name
        self._db = self.__client__.get_database("chatty")
        self._collection = self._db[self.collection_name]

    def insert_document(self, data:dict) -> Any | None:
        result =  self._collection.insert_one(data)
        if result.acknowledged:
            logger.info(f'Inserted document with id {result.inserted_id}')
            return result.inserted_id
        logger.error(f'Could not insert the document: {data}')
        return None

    def insert_many_documents(self, data:list[dict]) -> list | None:
        result = self._collection.insert_many(data)
        if result.acknowledged:
            logger.info(f'Inserted document with id {result.inserted_ids}')
            return result.inserted_ids
        logger.error(f'Could not insert the document: {data}')
        return None

    def get_document_by_id(self, _id:Any) -> dict:
        document =  self._collection.find_one({"_id": ObjectId(_id)})
        logger.info(f'Queried document with id {_id}')
        return document

    def get_all_documents(self) -> list[dict]:
        documents = []
        for document in self._collection.find():
            document["_id"] = str(document["_id"])
            documents.append(document)
        logger.info('Queried all documents')
        return documents

    def count(self) -> int:
        return self._collection.count_documents({})

    def update_document(self, _id:Any, update:dict) -> dict | None:
        query = {"_id": ObjectId(_id)}
        data = {"$set": update}
        updated = self._collection.find_one_and_update(query, data)
        logger.info(f'Updated document with id {_id}')
        return updated

    def delete_document(self, _id:Any):
        query = {"_id": ObjectId(_id)}
        self._collection.find_one_and_delete(query)
        logger.info(f'Deleted document with id {_id}')

    def count_with_query(self, query:dict) -> int:
        return self._collection.count_documents(query)
