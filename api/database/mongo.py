from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db = MongoClient(os.getenv("URL")).get_database("Barcelona")

def desempleo_by_all(collection, filter = {}, project = {"_id":0}, limit = 0, skip = 0):
    return db[collection].find(filter, project).limit(limit).skip(skip)
