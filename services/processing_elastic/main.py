from services.processing_elastic.manager import pull_kafka, insert_elastic


def main():
    data_files = pull_kafka()
    insert_elastic(data_files)

if __name__ == "__main__":
    main()