from connections.kafka_connection import create_consumer

class Consumer:
    def __init__(self , topic_name:str , group_id:str=None, auto_offset_reset="earliest"):
        self.consumer = create_consumer(topic_name , group_id , auto_offset_reset)

    def _consumer(self):
        print("Starting consumer...")
        for message in self.consumer:
            msg = message.value
            print(msg)