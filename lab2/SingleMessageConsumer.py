from confluent_kafka import Consumer
from confluent_kafka import serialization

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "single_group",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": True, # Автоматический коммит включен
    "auto.commit.interval.ms": 1000 # Интервал коммита

}
consumer = Consumer(conf)

consumer.subscribe(["lab2-topic"])

string_deserializer = serialization.StringDeserializer("utf_8")
try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Ошибка: {msg.error()}")
            continue

        key = string_deserializer(msg.key(), None)
        value = string_deserializer(msg.value(), None)
        print(f"Получено сообщение: {key=}, {value=}, offset={msg.offset()}")
finally:
    consumer.close()
