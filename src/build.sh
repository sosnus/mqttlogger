#!/bin/bash
# docker build --tag sosnus15/mqttlogger .
docker build --platform arm64 --tag sosnus15/mqttlogger .
docker push sosnus15/mqttlogger
docker pull sosnus15/mqttlogger
# sudo docker run --rm --name mqttlogger_container sosnus15/mqttlogger
sudo docker run --rm -e V_BROKER=127.0.0.1 -e V_PORT=1883 -e V_DB_PATH=/tmp/testdir/mqtt-logs/ --name mqttlogger_container sosnus15/mqttlogger