#THIS IS THE SUBSCRIBER CODE FOR EXERCISE 8 - Clean Session and QoS Testing
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("="*50)
    print("Message Topic:", message.topic)
    print("Message Received:", message.payload.decode())
    print("QoS Level:", message.qos)
    print("="*50)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        # we should always subscribe from on_connect callback to be sure
        # our subscribed is persisted across reconnections.
        print("Connected with result code "+str(reason_code))
        print("Subscribing to test topics with QoS=1...")
        # Subscribe with QoS 1 to test persistent sessions
        client.subscribe("test/qos/scenario1", 1)
        client.subscribe("test/qos/scenario2", 1)

# Initialize MQTT client with persistent session (clean_session=False)
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, clean_session=False, client_id="subscriber_exercise8")
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.user_data_set([])
mqttc.connect('localhost', 1883) #HERE YOU SHOULD SPECIFY THE BROKER IP

print("Subscriber started with clean_session=False (persistent session)")
print("Client ID: subscriber_exercise8")


try:
    mqttc.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber disconnecting...")
    mqttc.disconnect()
    mqttc.loop_stop()
