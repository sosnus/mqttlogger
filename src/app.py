import paho.mqtt.client as mqtt
import sqlitehelper as sqlitehelper
import os

##### VARIABLES START ######
# Define the MQTT broker and port
broker = os.getenv("V_BROKER")
db_path = "/tmp/mqttlogger/mqtt-logs/"
if broker == None:
    broker = "192.168.88.203"
##### VARIABLES END  ######

print(">>> build time: 2024-06-29v09")
print(">>> === RUN MQTTLOGGER (app.py) ===")
print(">>> app.py params: broker, db_path")
print(broker)
print(db_path)
sqlitehelper.check_path(db_path)
with open(db_path+"init_log.txt", "w") as file:
    file.write("mqttlogger-run!")
topic_str = "controller,datacollector,mobile,var,varfast"
topic_list = topic_str.split(',')
topics = list((str(item)+"/#", 0) for item in topic_list)

print(f">>> subscribe topics raw: {topic_str}")
print(f">>> subscribe topics list: {topics}")

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    message_payload = message.payload.decode('utf-8',errors='replace')
    sqlitehelper.insert_message(message_payload, message.topic)
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
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,protocol=mqtt.MQTTv5)

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

sqlitehelper.init_db(db_path)
message = "Init logger!"
topic = "mqttlogger/ok"
sqlitehelper.insert_message(message, topic)

# Connect to the MQTT broker
client.connect(broker, 1883, 60)

# Start the MQTT client loop to process network traffic and dispatch callbacks
client.loop_forever()