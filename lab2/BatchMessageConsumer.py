from confluent_kafka import Consumer
from confluent_kafka import serialization

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "batch_group",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False
}
consumer = Consumer(conf)

consumer.subscribe(["lab2-topic"])

string_deserializer = serialization.StringDeserializer("utf_8")


try:
    while True:

        messages = consumer.consume(num_messages=10, timeout=30.0)


        if not messages:
            continue

        for msg in messages:
            if msg is None:
                continue
            if msg.error():
                print(f"Ошибка: {msg.error()}")
                continue

            key = string_deserializer(msg.key(), None)
            value = string_deserializer(msg.value(), None)
            print(f"Получено сообщение: {key=}, {value=}, offset={msg.offset()}")
            last_msg = msg
        if last_msg is not None:
            try:
                consumer.commit(message=last_msg, asynchronous=False)
                print(f"Оффсет {last_msg.offset()} закоммичен")
            except Exception as e:
                print(f"Ошибка коммита: {e}")


finally:
    consumer.close()
