import json
import time

from kafka import KafkaProducer
from constants import KAFKA_SERVER_URL, KAFKA_TOPICS

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER_URL,
    value_serializer=lambda m: json.dumps(m).encode("utf-8"),
)


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    print("Error occured: ", exc_info=excp)


print("Starting to send sample texts...")

for i in range(1, 11):
    print("--------------------")
    topic = next(KAFKA_TOPICS)
    print(f"Sending data {i} to topic {topic}...")
    data = {"text": f"This is sample text - {i}"}
    producer.send(topic=topic, value=data).add_callback(on_send_success).add_errback(
        on_send_error
    )
    time.sleep(1)
