#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json
import requests
import datetime
from random import randint
import time

headerTL = {'Fiware-Service': 'icai23944',
            'Fiware-ServicePath': '/environment/Cross1'
            }
urlTL = 'http://130.206.112.29:1026/v2/entities/TL1/attrs/Light_info/value'
start_time = time.time()
numcoches=0
mqttc = mqtt.Client()
mqttc.connect('130.206.112.29', 1883)
while 1:
    a=1
    while (time.time() - start_time)<6:
        if a==1:
            r = requests.get(urlTL, headers=headerTL)
            a=a+1
    a=1
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    if r.json()== 'Green':
        numcoches=0
    if r.json()=='Red':
        numcoches=numcoches+randint(0,6)
    else:
        print "error"

    mqttc.publish("/1234/Dev23944TL1/attrs", json.dumps({"Nc":str(numcoches)}))
