#!/bin/bash
tag="v17"
echo $tag
# sudo docker build --tag sosnus15/mqttlogger:v04 .
# sudo docker push sosnus15/mqttlogger
docker build --platform arm64 --tag sosnus15/mqttlogger:$tag .
docker build --platform arm64 --tag sosnus15/mqttlogger .
sudo docker push sosnus15/mqttlogger:latest
sudo docker push sosnus15/mqttlogger:$tag
sudo docker pull sosnus15/mqttlogger
# https://github.com/sosnus/mqttlogger