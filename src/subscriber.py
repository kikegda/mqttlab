#THIS IS THE SUBSCRIBER CODE
import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):

    print("Message Topic:", message.topic)
    print("Message Received:", message.payload.decode())

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        # we should always subscribe from on_connect callback to be sure
        # our subscribed is persisted across reconnections.
        print("Connected with result code "+str(reason_code))
        # Subscribe to all topics from both publishers
        client.subscribe("spain/+/+")
        client.subscribe("france/+/+")
        # Subscribe to LWT status topics
        client.subscribe("status/#")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message


mqttc.user_data_set([])
mqttc.connect('localhost', 1883) #HERE YOU SHOULD SPECIFY THE BROKER IP

# Stay connected for 5 minutes and then disconnect gracefully
mqttc.loop_start()
print("Subscriber connected. It will disconnect in 5 minutes...")
time.sleep(300)
mqttc.disconnect()
mqttc.loop_stop()
print("Subscriber disconnected gracefully after 5 minutes")
print(f"Received the following message: {mqttc.user_data_get()}")