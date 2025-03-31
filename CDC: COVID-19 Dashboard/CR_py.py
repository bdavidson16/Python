from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from bson.son import SON
import pandas as pd
import requests

class CRUD_DB(object):
    def __init__(self):
        uri = "mongodb+srv://baileydavidson16:wwGlEMmsONyfvJw3@cluster0.lmhgaan.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        self.db = self.client["cdc_database"]
        self.collection = self.db["cdc_collection"]

# CREATE.
    def create_db(self, data):
        if data is not None and not data.empty:
            data_dict = data.to_dict(orient="records")  

            if isinstance(data_dict, list) and len(data_dict) > 0:
                result = self.collection.insert_many(data_dict)
                print(f"Insert Success: {result.acknowledged}")  
            else:
                raise Exception("Data conversion failed. No valid records found.")       
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# READ.
    def read(self, query={}):
        records = list(self.collection.find(query))
        return records

# FILTER.
    def filter_read(self, query):
        if query is not None:
            result = self.collection.find({"year": query})
            return list(result)   
        else:
            return []
            raise Exception("Nothing found, because list is empty")

# UPDATE
    def update_many(self, query, new_data):
        if query is not None:
            result = self.collection.update_many(data, {"$set": new_data})
            return result.modified_count
        else:
            raise Exception("Could not update data.")

# DELETE
    def delete_one(self, query):
        if query is not None:
            result = self.collection.delete_one(query)
            print(f"Deleted {result.deleted_count} document(s)")
            return result.deleted_count
        else:
            raise Exception("Could not delete data.")
            
