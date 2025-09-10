import os
from dotenv import load_dotenv
from loging.logger import Logger
from services.files.file_path import get_files_path_in_folder
from services.files.metadata import metadata_by_file_path
from services.service_metadata.produser import Producer

logger = Logger.get_logger()
producer = Producer()
load_dotenv()

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