import json
import time

from kafka import KafkaProducer
from constants import KAFKA_SERVER_URL, SAMPLE_KAFKA_TOPIC

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER_URL)

print("Starting to send sample texts...")

for i in range(1, 11):
    print(f"Sending data {i}...")
    data = {"text": f"This is sample text - {i}"}
    producer.send(topic=SAMPLE_KAFKA_TOPIC, value=json.dumps(data).encode("utf-8"))
    print(f"Done: data {i} sent!")
    time.sleep(1)
