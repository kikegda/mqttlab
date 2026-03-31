#THIS IS THE PUBLISHER CODE FOR EXERCISE 8 - Scenario 2: QoS = 1
import time
import paho.mqtt.client as mqtt

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Configure keepalive
mqttc.connect('localhost', 1883, keepalive=60) #HERE YOU SHOULD SPECIFY THE BROKER IP
mqttc.loop_start()

# Publish messages with QoS 1
messages = [
    ("test/qos/scenario2", "Message 2 with QoS=1", 1),
]

print("="*50)
print("Publisher initialized for EXERCISE 8 - Scenario 2")
print("Publishing with QoS = 1")
print("="*50)

for topic, payload, qos in messages:
    msg = mqttc.publish(topic, payload, qos, retain=False)
    msg.wait_for_publish()
    print(f"Published -> Topic: {topic}")
    print(f"            Payload: {payload}")
    print(f"            QoS: {qos}")
    print(f"            Retain: False")

print("\nMessage published. Waiting 2 seconds before disconnecting...")
time.sleep(2)

mqttc.disconnect()
mqttc.loop_stop()
print("Publisher disconnected.\n")
