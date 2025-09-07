import os
from datetime import datetime
from pathlib import Path

def get_files_path_in_folder(folder_path):
    files = []
    folder_path = Path(folder_path)
    for file in folder_path.iterdir():
        if file.is_file():
            files.append(os.path.join(folder_path, file))
    return files


def metadata_by_file_path(file_path):

    metadata = {}
    file_path = Path(file_path)
    if file_path.exists():
        file_stats = file_path.stat()
        metadata["name"] = file_path.name
        metadata["size"] = file_stats.st_size
        metadata["creation_date"] = datetime.fromtimestamp(file_stats.st_ctime)
        metadata["last_modified_date"] = datetime.fromtimestamp(file_stats.st_mtime)

    return metadata
