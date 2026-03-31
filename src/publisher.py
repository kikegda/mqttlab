#THIS IS THE PUBLISHER CODE
import time
import paho.mqtt.client as mqtt

unacked_publish = set()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqttc.connect('localhost', 1883) #HERE YOU SHOULD SPECIFY THE BROKER IP
mqttc.loop_start()

# Our application produce some messages

#better format to escalate more messages
messages = [
    ("spain/madrid/temp", "20C"),
    ("spain/madrid/humidity", "60%"),
]



# Wait for all message to be published
while len(unacked_publish):
    time.sleep(0.1)

# Due to race-condition described above, the following way to wait for all publish is safer
for topic, payload in messages:
    msg = mqttc.publish(topic, payload, 0, True)
    msg.wait_for_publish()
    print(f"Published -> {topic}: {payload}")

mqttc.disconnect()
mqttc.loop_forever()