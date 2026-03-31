#THIS IS THE PUBLISHER CODE
import time
import random
import paho.mqtt.client as mqtt

unacked_publish = set()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

LWT_TOPIC = "status/spain/madrid/publisher1"
LWT_MESSAGE = "Publisher1 disconnected unexpectedly"

# Configure Last Will and Testament before connecting
mqttc.will_set(LWT_TOPIC, LWT_MESSAGE, qos=0, retain=False)

# Configure keepalive to 30 seconds to observe frequent keepalive messages
mqttc.connect('localhost', 1883, keepalive=30) #HERE YOU SHOULD SPECIFY THE BROKER IP
mqttc.loop_start()

# Publish temperature each 30 seconds (10 messages in 5 minutes)
print("Publisher started. Sending random temperature every 30 seconds...")
for i in range(10):
    temp_value = random.randint(10, 30)
    payload = str(temp_value) + "C"

    msg = mqttc.publish("spain/madrid/temp", payload, qos=0, retain=False)
    msg.wait_for_publish()

    print(f"[{i+1}/10] Published -> spain/madrid/temp: {payload}")
    time.sleep(30)

mqttc.disconnect()
mqttc.loop_stop()