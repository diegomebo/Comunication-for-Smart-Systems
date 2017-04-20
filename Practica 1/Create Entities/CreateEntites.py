#!/usr/bin/env python
# This programm create all the entities for this practice.

import requests
import json

urlCross = 'http://130.206.112.29:1026/v2/entities'
headersw = {'Fiware-Service': 'icai23944'}
headerCross1 = {'Fiware-Service': 'icai23944',
                'Fiware-ServicePath': '/environment',
                'Content-type': 'application/json'
                }
payloadCross1 = {"id": "Cross1",
                 "type": "Cross",
                 "Location": {
                     "type": "geo:point",
                     "value": "40.4307 , -3.7163",
                     "metadata":{
                        "StreetNames":{
                        "type":"string",
                        "value":{
                         "street1":"Alberto_Aguilera",
                         "street2":"Pricesa"
                            }
                         }
                     }
                 },
                 "NumTL": {
                     "type": "int",
                     "value": "4"
                 }
                 }
# r = requests.post(url,headers=headers,json=(payload))
# r = requests.post(urlCross, headers=headerCross1, json=(payloadCross1))

urlTL = 'http://130.206.112.29:5050/iot/devices'
headerTL = {'Fiware-Service': 'icai23944',
            'Fiware-ServicePath': '/environment/Cross1',
            'Content-type': 'application/json'
            }
payloadTL1 = {
    "devices":[
        {
            "device_id": "Dev23944TL1",
            "entity_name": "TL1",
            "entity_type": "TL",
            "transport": "MQTT",
            "attributes": [
                {"object_id": "Nc", "name": "NumCars", "type": "int"}
            ],
            "commands": [
                {"object_id": "L", "name": "Light", "type": "binary"}
            ],
            "static_attributes": [
                {"name": "Direction", "type": "Char", "value": "N"}
            ]
        }
    ]
}
payloadTL2 = {
    "devices":[
        {
            "device_id": "Dev23944TL2",
            "entity_name": "TL2",
            "entity_type": "TL",
            "transport": "MQTT",
            "attributes": [
                {"object_id": "Nc", "name": "NumCars", "type": "int"}
            ],
            "commands": [
                {"object_id": "L", "name": "Light", "type": "binary"}
            ],
            "static_attributes": [
                {"name": "Direction", "type": "Char", "value": "W"}
            ]
        }
    ]
}
payloadTL3 = {
    "devices":[
        {
            "device_id": "Dev23944TL3",
            "entity_name": "TL3",
            "entity_type": "TL",
            "transport": "MQTT",
            "attributes": [
                {"object_id": "Nc", "name": "NumCars", "type": "int"}
            ],
            "commands": [
                {"object_id": "L", "name": "Light", "type": "binary"}
            ],
            "static_attributes": [
                {"name": "Direction", "type": "Char", "value": "S"}
            ]
        }
    ]
}
payloadTL4 = {
    "devices":[
        {
            "device_id": "Dev23944TL4",
            "entity_name": "TL4",
            "entity_type": "TL",
            "transport": "MQTT",
            "attributes": [
                {"object_id": "Nc", "name": "NumCars", "type": "int"}
            ],
            "commands": [
                {"object_id": "L", "name": "Light", "type": "binary"}
            ],
            "static_attributes": [
                {"name": "Direction", "type": "Char", "value": "E"}
            ]
        }
    ]
}
r= requests.post(urlTL, headers=headerTL, json=(payloadTL1))
r= requests.post(urlTL, headers=headerTL, json=(payloadTL2))
r= requests.post(urlTL, headers=headerTL, json=(payloadTL3))
r= requests.post(urlTL, headers=headerTL, json=(payloadTL4))
try:
    print r.status_code
    print json.dumps(r.json(), indent=4)
except:
    pass
