import json

from elastic.elastic import Elastic
from kafka1.consumer import Consumer
from services.file_path import get_files_path_in_folder, metadata_by_file_path, convert_dict_to_json
from kafka1.produser import Producer

producer = Producer()

path_files = get_files_path_in_folder("C:\podcasts")
dict_data_file = {}
for path_file in path_files:
    dict_data_file["path_file"] = path_file
    dict_data_file['metadata'] = metadata_by_file_path(path_file)
    json_data_file = convert_dict_to_json(dict_data_file)
    producer.send_message(json_data_file, "data_file")

consumer = Consumer('data_file')
data = consumer._consumer()
ela = Elastic('metadata_of_files')

list_dict = []
for value in data:
    json_load = json.loads(value)
    json_load["Unique ID"] = json_load['metadata']['size']
    list_dict.append(list_dict)

ela.insert_docs(list_dict)
