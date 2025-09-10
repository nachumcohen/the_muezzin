import os
from pathlib import Path

def get_files_path_in_folder(folder_path):
    path_files = []
    folder_path = Path(folder_path) # Path - provides methods for use on the path
    for file in folder_path.iterdir(): # iterdir() - return the contents of the library (children)
        if file.is_file():
            path_files.append(os.path.join(folder_path, file)) # creating an absolute path
    return path_files
