# Centralized management of kafka topics PoC

    docker build . -t kafka-topics
    docker run -it --rm -e BOOTSTRAP_SERVERS=kafka:9092 kafka-topics
