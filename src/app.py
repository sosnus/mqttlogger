import paho.mqtt.client as mqtt
# import sqlitehelper as datawriter
import csvhelper as datawriter
import os
import time
from datetime import datetime

##### VARIABLES START ######
# Define the MQTT broker and port
broker = os.getenv("V_BROKER")
topic_str = os.getenv("V_TOPICS")
# topic_str = "controller,datacollector,mobile,var,varfast,logs,status" # example
db_path = "/tmp/mqttlogger/mqtt-logs/"
version = "v2.1.20___2025-08-08"
# if broker == None:
    # broker = "192.168.88.203"
if topic_str == None:
    print(">>> [ERR] NO topic_str PARAM!")
    topic_str = "controller,datacollector,mobile,var,varfast,status" # example
    # topic_str = "controller,datacollector,mobile,var,varfast,logs,status" # example
    time.sleep(1)
if broker == None:
    print(">>> [ERR] NO broker PARAM!")
    broker = "192.168.88.202" # example
    time.sleep(1)
##### VARIABLES END  ######

print(f">>> build version & time: {version}")
print(">>> === RUN MQTTLOGGER (app.py) ===")
print(">>> app.py params: broker, db_path")
print(broker)
print(db_path)
datawriter.check_path(db_path)
with open(db_path+"init_log.txt", "w") as file:
    file.write(version)
    file.write(broker)
    file.write(topic_str)
topic_list = topic_str.split(',')
topics = list((str(item)+"/#", 0) for item in topic_list)

print(f">>> subscribe topics raw: {topic_str}")
print(f">>> subscribe topics list: {topics}")

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    message_payload = message.payload.decode('utf-8',errors='replace')
    datawriter.insert_message(message_payload, message.topic)
    client.publish("mqttlogger/mqttlogger", f"msg from {message.topic} len={len(message_payload)} logged")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    print(f">>> msg from {message.topic} len={len(message_payload)} logged {datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}")
    # print(f">>> msg from {message.topic} len={len(message_payload)} logged {timestamp}")
# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(">>> Connected successfully")
        client.publish("mqttlogger/mqttlogger", "Connected successfully")
        datawriter.insert_message("Connected successfully", "mqttlogger/ok")
        datawriter.insert_message(str(topics), "mqttlogger/subscribed_topics")
        # Subscribe to the topic
        client.subscribe(topics)
    else:
        print(f">>> Connect failed with code {rc}")
        datawriter.insert_message("Connect failed with code {rc}", "mqttlogger/error")

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,protocol=mqtt.MQTTv5)

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

datawriter.init_db(db_path)
message = "Init logger!"
topic = "mqttlogger/ok"
datawriter.insert_message(message, topic)

# Connect to the MQTT broker
client.connect(broker, 1883, 60)

# Start the MQTT client loop to process network traffic and dispatch callbacks
client.loop_forever()