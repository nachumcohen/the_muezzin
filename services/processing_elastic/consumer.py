from connections.kafka_connection import create_consumer
from loging.logger import Logger

logger = Logger.get_logger()

class Consumer:
    def __init__(self , topic_name:str , group_id:str=None, auto_offset_reset="earliest"):
        self.consumer = create_consumer(topic_name , group_id , auto_offset_reset)


    def stop_consumers(self):
        self.consumer.close()

    def run_consumer(self):
        logger.info("Starting consumer...")
        for message in self.consumer:
            yield message.value