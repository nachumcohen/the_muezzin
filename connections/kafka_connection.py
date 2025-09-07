import os
from dotenv import load_dotenv
import json
from kafka import KafkaConsumer, KafkaProducer

load_dotenv()

def create_consumer(topic_name, group_id=None, auto_offset_reset="earliest"):
    """
    Return KafkaConsumer ready to read from a topic
    """
    return KafkaConsumer(
        topic_name,
        bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset=auto_offset_reset,
        group_id=group_id or f"group_{topic_name}",
        enable_auto_commit=True
    )

def create_producer():
    """
    Returns a KafkaProducer ready to send to a Topic
    """
    return KafkaProducer(
        bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )