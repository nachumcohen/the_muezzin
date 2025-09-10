import os
from dotenv import load_dotenv

from loging.logger import Logger
from services.fiels.convert_audio_files import convert_audio_to_text
from services.processing_elastic.consumer import Consumer
from services.processing_elastic.elastic_dal import Elastic

load_dotenv()
topic = os.getenv('TOPIC')
logger = Logger.get_logger()
elastic = Elastic('metadata_of_files2')

def pull_kafka():
    consumer = Consumer(topic , "listener_elastic2")
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