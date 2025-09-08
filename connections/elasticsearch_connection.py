import os
from dotenv import load_dotenv

load_dotenv()

def create_elasticsearch():
    elasticsearch = os.getenv('ELASTIC_SERVER')
    return elasticsearch




