#!/bin/bash
docker build --tag sosnus15/mqttlogger .
# docker build --platform arm64 --tag sosnus15/mqttlogger .
docker push sosnus15/mqttlogger
# sudo docker run --rm --name mqttlogger_container sosnus15/mqttlogger
sudo docker run --rm -e V_BROKER=10.10.10.210 -e VURL=google.com -e V_PORT=1883 -e V_DB_PATH=/tmp/testdir/mqtt-logs/ --name mqttlogger_container sosnus15/mqttlogger
