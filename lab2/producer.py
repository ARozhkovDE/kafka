from confluent_kafka import Producer
from confluent_kafka import serialization
import random
import json

conf = {
    "bootstrap.servers": "localhost:9092",
    "acks":"all",
    "retries":3
} 


producer = Producer(conf)

string_serializer = serialization.StringSerializer("utf_8")

for _ in range(5):
    key = string_serializer('key-1', None)
    value = string_serializer(f"message-{random.randint(1,99999)}", None)

    producer.produce(
        topic="lab2-topic",
        key=key,
        value=value,
)

producer.flush()
