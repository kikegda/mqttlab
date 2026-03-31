#THIS IS THE SUBSCRIBER CODE
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
        # client.subscribe("paho/test/topic")
        client.subscribe("spain/madrid/temp")
        client.subscribe("spain/madrid/humidity")
        # client.subscribe("spain/madrid/pressure")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message


mqttc.user_data_set([])
mqttc.connect('localhost', 1883) #HERE YOU SHOULD SPECIFY THE BROKER IP
mqttc.loop_forever()
print(f"Received the following message: {mqttc.user_data_get()}")