export COMPOSE_HTTP_TIMEOUT=600
docker-compose down
docker system prune -a -f --volumes
docker-compose up -d



topic_name=lab2-topic

docker exec lab_2_kafka1_1 \
  /bin/kafka-topics --delete \
  --topic $topic_name \
  --bootstrap-server localhost:29092

docker exec lab_2_kafka1_1 \
  /bin/kafka-topics --create \
  --topic $topic_name \
  --partitions 3 \
  --replication-factor 2 \
  --bootstrap-server localhost:29092


