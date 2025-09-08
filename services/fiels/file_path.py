import os
from pathlib import Path

def get_files_path_in_folder(folder_path):
    files = []
    folder_path = Path(folder_path)
    for file in folder_path.iterdir():
        if file.is_file():
            files.append(os.path.join(folder_path, file))
    return files
