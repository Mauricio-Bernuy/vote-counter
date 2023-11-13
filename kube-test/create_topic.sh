#/bin/bash

kafka-topics.sh --create --topic numtest --partitions 1 --bootstrap-server kafka:9092 || kafka-topics.sh --alter --topic numtest --partitions 4 --bootstrap-server kafka:9092

echo "topic numtest was create"