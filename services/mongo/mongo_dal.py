import gridfs
from connections.mongo_connection import create_mongo_client
from logger import Logger

logger = Logger.get_logger()

class MongoDAL:

    def __init__(self):
        self.db = create_mongo_client()

    def store_file_audio(self,file_path, id):
        fs = gridfs.GridFS(self.db)

        with open(file_path, 'rb') as f:
            file_id = fs.put(f, unique_id=id)

        logger.info(f"stored successfully with ID: {file_id}")