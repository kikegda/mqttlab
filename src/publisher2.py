#THIS IS THE SECOND PUBLISHER CODE - Testing with different keepalive value
import time
import paho.mqtt.client as mqtt

unacked_publish = set()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Configure keepalive to 120 seconds to observe less frequent keepalive messages
mqttc.connect('localhost', 1883, keepalive=120) #HERE YOU SHOULD SPECIFY THE BROKER IP
mqttc.loop_start()

# Our application produce some messages with different topics
messages = [
    ("france/paris/temp", "18C"),
    ("france/paris/humidity", "65%"),
]

# Wait for all message to be published
while len(unacked_publish):
    time.sleep(0.1)

# Due to race-condition described above, the following way to wait for all publish is safer
for topic, payload in messages:
    msg = mqttc.publish(topic, payload, 0, True)
    msg.wait_for_publish()
    print(f"Published -> {topic}: {payload}")

# Keep the client connected for 5 minutes to observe keepalive messages
print("Client connected with keepalive=120s. Staying connected for 5 minutes to observe keepalive behavior...")
time.sleep(300)

mqttc.disconnect()
mqttc.loop_stop()
