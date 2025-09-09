from logger import Logger
from services.elastic.elastic_dal import Elastic
from services.fiels.convert_audio_files import convert_audio_to_text
from services.fiels.metadata import metadata_by_file_path
from services.kafka.consumer import Consumer
from services.fiels.file_path import get_files_path_in_folder
from services.kafka.produser import Producer
from services.mongo.mongo_dal import MongoDAL
import os
from dotenv import load_dotenv

load_dotenv()

logger = Logger.get_logger()
producer = Producer()
mongo_dal = MongoDAL()
elastic = Elastic('metadata_of_files')

path_folder = os.getenv('PATH_FOLDER')
topic = os.getenv('TOPIC')

def _created_id_by_metadata(metadata:dict):
    id = hash(f"{metadata['name']}{metadata['last_modified_date']}{metadata['size']}{metadata['id_owner']}")
    return id

def return_list_of_dicts_with_metadata_and_pathfile_by_folder(folder:str = path_folder):
    path_files = get_files_path_in_folder(folder)
    list_data_files = []
    for path_file in path_files:
        dict_data_file = dict()
        metadata = metadata_by_file_path(path_file)
        unique_id = _created_id_by_metadata(metadata)
        dict_data_file["path_file"] = path_file
        dict_data_file['metadata'] = metadata
        dict_data_file['unique_id'] = unique_id
        list_data_files.append(dict_data_file)
    return list_data_files


def insert_kafka(list_data_files:list):
    for data_file in list_data_files:
        try:
          producer.send_message(data_file, topic)
          logger.info(f"{data_file['metadata']['name']} ,data_file(path_file + metadata) go to kafka")
        except Exception as e:
            logger.error(f"{data_file['metadata']['name']}, {e}")

def pull_kafka():
    consumer = Consumer(topic)
    data_files = [value for value in consumer.run_consumer()]
    consumer.stop_consumers()
    return data_files


def insert_elastic(data_files:list[dict]):
    list_dict = []
    for data_file in data_files:
        path_file = data_file["path_file"]

        if data_file['metadata']['size'] > 0:
            text = convert_audio_to_text(path_file)
            data_file['metadata']["text"] = text
            logger.info(f"{data_file['metadata']['name']}, Text successfully added")

        else:
            data_file['metadata']["text"] = None
            logger.info(f"{data_file['metadata']['name']}, non text")
        list_dict.append(data_file)

    elastic.insert_docs(list_dict)

def insert_mongo(data_files:list[dict]):

    for data_file in data_files:
        try:
            path_file = data_file["path_file"]
            id = data_file['unique_id']
            mongo_dal.store_file_audio(path_file , id)
            logger.info(f"{data_file['metadata']['name']}, insert mongo successfully")

        except Exception as e:
            logger.error(f"{data_file['metadata']['name']}, {e}")