import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_mongo_client():
    """
    :return: connection to mongodb
    """
    mongo_server = os.getenv('MONGO_SERVER')
    db_name = os.getenv('db_name')
    client = MongoClient(mongo_server)
    db = client[db_name]
    return db