FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY processing/ .
COPY connections/kafka_connection.py ./connections
COPY connections/elasticsearch_connectio.py ./connections
COPY files/ .
copy loging/ .

CMD ["python3", "main.py"]