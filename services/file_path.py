import json
import os
from pathlib import Path

def get_files_path_in_folder(folder_path):
    files = []
    folder_path = Path(folder_path)
    for file in folder_path.iterdir():
        if file.is_file():
            files.append(os.path.join(folder_path, file))
    return files


def metadata_by_file_path(file_path):

    metadata_dict = {}
    file_path = Path(file_path)
    if file_path.exists():
        file_stats = file_path.stat()
        metadata_dict["name"] = file_path.name
        metadata_dict["size"] = file_stats.st_size
        metadata_dict["creation_date"] = file_stats.st_ctime
        metadata_dict["last_modified_date"] = file_stats.st_mtime

    return metadata_dict


def convert_dict_to_json(dict_to_convert : dict):
    dict_to_json = json.dumps(dict_to_convert)
    return dict_to_json
