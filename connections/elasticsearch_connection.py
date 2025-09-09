import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch


load_dotenv()

def create_elasticsearch():
    """
    :return: connection to elasticsearch
    """
    elasticsearch = os.getenv('ELASTIC_SERVER')
    return Elasticsearch(elasticsearch)




