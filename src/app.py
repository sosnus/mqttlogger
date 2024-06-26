import paho.mqtt.client as mqtt
import sqlitehelper as sqlitehelper
import os

##### VARIABLES START ######
# Define the MQTT broker and port
broker = os.getenv("V_BROKER")
db_path = os.getenv("V_DB_PATH")
# port = os.getenv("V_PORT")
# db_path = "/tmp/testdir/mqtt-logs/"

print(">>> build time: 2024-06-26v03")
print(">>>=== RUN MQTTLOGGER (app.py) ===")
print(">>> app.py: broker, db_path")
print(broker)
# print(port)
print(db_path)
sqlitehelper.check_path(db_path)


# Define the topic to subscribe to
# topics = [("status/#", 0), ("var/#", 0)]
topics = [("status/#", 0), ("controller/#", 0), ("datacollector/#", 0), ("mobile/#", 0), ("var/#", 0), ("varfast/#", 0)]

##### VARIABLES END  ######

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}' with QoS {message.qos}")
    sqlitehelper.insert_message(message.payload.decode(), message.topic)
    client.publish("logs/mqttlogger", "new msg!")
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