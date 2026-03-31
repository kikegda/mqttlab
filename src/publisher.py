#THIS IS THE PUBLISHER CODE
import time
import paho.mqtt.client as mqtt

unacked_publish = set()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqttc.connect('localhost', 1883) #HERE YOU SHOULD SPECIFY THE BROKER IP
mqttc.loop_start()

# Our application produce some messages
msg2 = mqttc.publish("spain/madrid/temp", "20C", 1)
msg3 = mqttc.publish("spain/madrid/humidity", "60%", 2)
##msg4 = mqttc.publish("spain/madrid/pressure", "1013hPa")


# Wait for all message to be published
while len(unacked_publish):
    time.sleep(0.1)

# Due to race-condition described above, the following way to wait for all publish is safer
# for msg in [msg1, msg2, msg3, msg4]:
msg2.wait_for_publish()
msg3.wait_for_publish()

mqttc.disconnect()
mqttc.loop_forever()