from elasticsearch import helpers
from elasticsearch.helpers import BulkIndexError

from connections.elasticsearch_connection import create_elasticsearch
from loging.logger import Logger

logger = Logger.get_logger()

class Elastic:
    def __init__(self , index_name:str):
        self.es = create_elasticsearch() # get connection to elasticsearch
        self.index_name = index_name
        self.check_all_processed = False

    def create_mapping(self,mapping):
        self.es.indices.delete(index=self.index_name, ignore_unavailable=True)
        self.es.indices.create(index=self.index_name, mappings=mapping)

    def insert_docs(self, docs: list[dict]):
        actions = [
            {
                "_index": self.index_name,
                "_source": doc
            }
            for doc in docs
        ]
        try:
            helpers.bulk(self.es, actions)
            logger.info("insert successfully docs")

        except BulkIndexError as e:
            logger.error("Bulk error:", e)

    def get_all(self):
        query = {
            "query": {
                "match_all": {}
            },
        }
        results = self.es.search(index=self.index_name, body=query, size=10000)
        return results