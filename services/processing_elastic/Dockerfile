FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY services/processing_elastic/ .
COPY connections/ ./connections/kafka_connection.py
COPY connections/elasticsearch_connection.py ./connections
COPY services/files/ .files

CMD ["python3", "main.py"]