from connections.kafka_connection import create_producer


class Producer:

    def __init__(self):
      self.producer = create_producer()

    def send_message(self,data:dict , topic:str):
        self.producer.send(topic, data)
        self.producer.flush()