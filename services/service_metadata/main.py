from services.service_metadata.manager import return_list_of_dicts_with_metadata_and_pathfile_by_folder, insert_kafka



def main():
    data_file = return_list_of_dicts_with_metadata_and_pathfile_by_folder()
    insert_kafka(data_file)

if __name__ == "__main__":
    main()
