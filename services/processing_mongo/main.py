from services.processing_mongo.manager import pull_kafka, insert_mongo


def main():
    data_files = pull_kafka()
    insert_mongo(data_files)

if __name__ == "__main__":
    main()