from pathlib import Path

def metadata_by_file_path(file_path):

    metadata_dict = {}
    file_path = Path(file_path)
    if file_path.exists(): # checks if a file exists
        file_stats = file_path.stat() # stat is object containing detailed information about the file
        metadata_dict["name"] = file_path.name
        metadata_dict["size"] = file_stats.st_size # size in bytes
        metadata_dict["id_owner"] = file_stats.st_uid # user id of the owner
        metadata_dict["last_modified_date"] = file_stats.st_mtime # time of the last modification

    return metadata_dict