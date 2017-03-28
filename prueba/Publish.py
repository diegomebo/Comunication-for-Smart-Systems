#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json

mqttc = mqtt.Client()
mqttc.connect('130.206.112.29', 1883)
mqttc.publish("/1234/Dev23944TL1/cmdexe", json.dumps({"Light":"Red"}))
