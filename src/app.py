import paho.mqtt.client as mqtt
import sqlitehelper as sqlitehelper

##### VARIABLES START ######
# Define the MQTT broker and port
broker = "10.10.10.210"
port = 1883
# db_path = "/tmp/testdir/mqtt-logs/"
db_path = "../tmp/"

print("=== RUN MQTTLOGGER ===")
print(broker)
print(port)
print(db_path)

# Define the topic to subscribe to
# topics = [("status/#", 0), ("var/#", 0)]
topics = [("status/#", 0), ("var/#", 0)]
##### VARIABLES END  ######

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}' with QoS {message.qos}")
    sqlitehelper.insert_message(message.payload.decode(), message.topic)
# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected successfully")
        sqlitehelper.insert_message("Connected successfully", "mqttlogger/ok")
        # Subscribe to the topic
        client.subscribe(topics)
    else:
        print(f"Connect failed with code {rc}")
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
client.connect(broker, port, 60)

# Start the MQTT client loop to process network traffic and dispatch callbacks
client.loop_forever()