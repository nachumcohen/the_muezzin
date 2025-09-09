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
    id = hash(f"{metadata['name']}{metadata['last_modified_date']}{metadata['size']}")
    return id

def return_list_of_dicts_with_metadata_and_pathfile_by_folder(folder:str = path_folder):
    path_files = get_files_path_in_folder(folder)
    dict_data_file = {}
    list_data_files = []
    for path_file in path_files:
        dict_data_file["path_file"] = path_file
        dict_data_file['metadata'] = metadata_by_file_path(path_file)
        list_data_files.append(dict_data_file)
    return list_data_files[:3]


def insert_kafka(list_data_files:list):
    for data_file in list_data_files:
        try:
          producer.send_message(data_file, topic)
          logger.info("data_file(path_file + metadata) go to kafka")
        except Exception as e:
            logger.error(e)

def pull_kafka():
    consumer = Consumer(topic)
    data_files = [value for value in consumer.run_consumer()]
    consumer.stop_consumers()
    return data_files


def insert_elastic(data_files:list[dict]):
    list_dict = []
    for value in data_files:

        id = _created_id_by_metadata(value['metadata'])
        value["Unique_ID"] = id

        path_file = value["path_file"]
        if value['metadata']['size'] > 0:
            text = convert_audio_to_text(path_file)
            print(text)
            value['metadata']["text"] = text
        else:
            value['metadata']["text"] = None
        list_dict.append(value)

    elastic.insert_docs(list_dict)

def insert_mongo(data_files:list[dict]):

    for data_file in data_files:
        path_file = data_file["path_file"]
        id = _created_id_by_metadata(data_file['metadata'])
        mongo_dal.store_file_audio(path_file , id)