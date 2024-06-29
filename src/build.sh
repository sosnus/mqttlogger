#!/bin/bash
tag="v15"
echo $tag
# sudo docker build --tag sosnus15/mqttlogger:v04 .
docker build --platform arm64 --tag sosnus15/mqttlogger:$tag .
docker build --platform arm64 --tag sosnus15/mqttlogger .
sudo docker push sosnus15/mqttlogger:$tag
sudo docker push sosnus15/mqttlogger
sudo docker push sosnus15/mqttlogger:latest
sudo docker pull sosnus15/mqttlogger