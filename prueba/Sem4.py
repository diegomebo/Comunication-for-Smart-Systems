#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/1234/Dev23944TL4/cmd")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    mss=json.loads(msg.payload)
    if mss["Light"] == "0":
        mqttc.publish("/1234/Dev23944TL4/cmdexe", json.dumps({"Light": "Red"}))
    if mss["Light"] == "1":
        mqttc.publish("/1234/Dev23944TL4/cmdexe", json.dumps({"Light": "Green"}))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
mqttc = mqtt.Client()
mqttc.connect('130.206.112.29', 1883)

client.connect("130.206.112.29", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()