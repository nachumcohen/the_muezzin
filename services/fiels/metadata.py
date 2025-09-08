from pathlib import Path

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