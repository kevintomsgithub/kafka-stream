from kafka import KafkaConsumer
from constants import KAFKA_SERVER_URL, SAMPLE_KAFKA_TOPIC

consumer = KafkaConsumer(SAMPLE_KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER_URL)

print("Reading from Kafka...")

while True:
    for message in consumer:
        print("- message: ")
        print(message)
