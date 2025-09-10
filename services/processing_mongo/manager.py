import os
from dotenv import load_dotenv
from loging.logger import Logger
from services.processing_mongo.consumer import Consumer
from services.processing_mongo.mongo_dal import MongoDAL

load_dotenv()
topic = os.getenv('TOPIC')
logger = Logger.get_logger()
mongo_dal = MongoDAL()


def pull_kafka():
    consumer = Consumer(topic , "listener_mongo2")
    data_files = [value for value in consumer.run_consumer()]
    consumer.stop_consumers()
    return data_files

def insert_mongo(data_files:list[dict]):

    for data_file in data_files:
        try:
            path_file = data_file["path_file"]
            id = data_file['unique_id']
            mongo_dal.store_file_audio(path_file , id)
            logger.info(f"{data_file['metadata']['name']}, insert mongo successfully")

        except Exception as e:
            logger.error(f"{data_file['metadata']['name']}, {e}")