# TEH - MUEZZIN project

## The project process, 
    Kafka sends a list of dictionaries - including a path to the file and information such as the file name and size,
    Two listeners, one sends what it received to Elastic, and also sends the file for conversion to text,
    The second stores the path to the repository in Mongo.

## connection folders
    Returns connections to Kafka and Mongo, etc.

## logging
- logger.py - sends logging to elastic 

## services - The project code
- files - File and path service.
  - convert_audio , Converts audio file to text with the help of a library 'whisper'.
  - file_path, Accepts a path to a directory and returns all the paths to files within it, with the help of a library 'pathlib'.
  - metadata, Returns metadata about a file path, with the help of a library 'pathlib'.
- service_metadata - Creates metadata about a file and sends it to Kafka
- 
- processing_mongo,
   consumer listens to Kafka and sends a path to a file with conversion to bits, 
  and sends to Mongo with unique id.

- processing_elastic 
    Listens to Kafka and sends what it received to Elastic, 
    including converting the audio to text and adding an additional text field,
- 
    העדפתי לעשות שירות נוסף שהוא ימשוך ממונגו וימיר את הקובץ שמע לטקסט ויעדכן את אלסטיק אבל נתקלתי בשגיאות והתעכבתי עם הזמן אז הכנסתי אותו אחרי ההזנה לפני השליחה לאלסטיק