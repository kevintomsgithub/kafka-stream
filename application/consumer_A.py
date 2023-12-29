import json

from kafka import KafkaConsumer
from constants import KAFKA_SERVER_URL

consumer = KafkaConsumer(
    "A",
    bootstrap_servers=KAFKA_SERVER_URL,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)

print("Reading from Kafka...")

while True:
    for message in consumer:
        print(f"- message in A: {message.value}")
