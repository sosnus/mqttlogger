#!/bin/bash
docker build --tag sosnus15/mqttlogger .
# docker push sosnus15/mqttlogger
sudo docker run --rm --name mqttlogger_container sosnus15/mqttlogger
