#!/bin/bash
# sudo docker build --tag sosnus15/mqttlogger:v04 .
docker build --platform arm64 --tag sosnus15/mqttlogger:v07 .
sudo docker push sosnus15/mqttlogger:v07
sudo docker pull sosnus15/mqttlogger
# sudo docker run --rm --name mqttlogger_container sosnus15/mqttlogger
# sudo docker run --rm -e V_BROKER=127.0.0.1 -e V_PORT=1883 -e V_DB_PATH=/tmp/testdir/mqtt-logs/ --name mqttlogger_container sosnus15/mqttlogger