from itertools import cycle

import os

KAFKA_SERVER_URL = os.environ["KAFKA_SERVER"]
SAMPLE_KAFKA_TOPIC = "sample-topic"

KAFKA_TOPICS = cycle(["A", "B"])
