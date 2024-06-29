import paho.mqtt.client as mqtt
import sqlitehelper as sqlitehelper
import os
# temporary lib
import time

##### VARIABLES START ######
# Define the MQTT broker and port
broker = os.getenv("V_BROKER")
db_path = "/tmp/mqttlogger/mqtt-logs/"
# db_path = os.getenv("V_DB_PATH")
if broker == None:
    broker = "192.168.88.203"
    # db_path = "/tmp/mqttlogger/mqtt-logs/"


print(">>> build time: 2024-06-29v08")
print(">>> === RUN MQTTLOGGER (app.py) ===")
print(">>> app.py params: broker, db_path")
print(broker)
# print(port)
print(db_path)
sqlitehelper.check_path(db_path)
with open(db_path+"init_log.txt", "w") as file:
    file.write("mqttlogger-run!")
topic_str = "controller,datacollector,mobile,var,varfast"
topic_list = topic_str.split(',')
# ["controller","datacollector","mobile","var","varfast"]
print(topic_list)

# Define the topic to subscribe to
# topics = [("status/#", 0)]

topics2 = [("controller/#", 0), ("datacollector/#", 0), ("mobile/#", 0), ("var/#", 0), ("varfast/#", 0)]
# topics = [("status/#", 0), ("controller/#", 0), ("datacollector/#", 0), ("mobile/#", 0), ("var/#", 0), ("varfast/#", 0)]
topics = list((str(item)+"/#", 0) for item in topic_list)
##### VARIABLES END  ######

print(f">>> subscribe topics: {topic_list}")
print(f">>> subscribe topics: {topics}")
print(f">>> subscribe topics: {topics2}")
time.sleep(10)
# Define the callback function for when a message is received
def on_message(client, userdata, message):
    message_payload = message.payload.decode('utf-8',errors='replace')
    # message_payload = message_payload.
    # print(f"Received message '{message.payload.decode()}' on topic '{message.topic}' with QoS {message.qos}")
    # print(f">> Received message '{message.payload}' on topic '{message.topic}' with QoS {message.qos}")
    # print(f">> Received message '{message_payload}' on topic '{message.topic}' with QoS {message.qos}")
    sqlitehelper.insert_message(message_payload, message.topic)
    # sqlitehelper.insert_message(message.payload.decode(), message.topic)
    client.publish("logs/mqttlogger", f"msg from {message.topic} len={len(message_payload)} logged")
    print(f">>> msg from {message.topic} len={len(message_payload)} logged")
# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(">>> Connected successfully")
        client.publish("logs/mqttlogger", "Connected successfully")
        sqlitehelper.insert_message("Connected successfully", "mqttlogger/ok")
        # Subscribe to the topic
        client.subscribe(topics)
    else:
        print(f">>> Connect failed with code {rc}")
        sqlitehelper.insert_message("Connect failed with code {rc}", "mqttlogger/error")


# Create an MQTT client instance
# client = mqtt.Client()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,protocol=mqtt.MQTTv5)

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

sqlitehelper.init_db(db_path)
# received_time = datetime.now()
message = "Init logger!"
topic = "mqttlogger/ok"
sqlitehelper.insert_message(message, topic)

# Connect to the MQTT broker
# client.connect(broker, 60)
client.connect(broker, 1883, 60)
# client.connect(broker, port, 60)

# Start the MQTT client loop to process network traffic and dispatch callbacks
client.loop_forever()