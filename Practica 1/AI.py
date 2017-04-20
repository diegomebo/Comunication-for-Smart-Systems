#!/usr/bin/env python
# This program is the IA for the crosses
# It use NGSI protocol


import requests
import json
import time

# variables for the directions and headers and payloads

UrlTL1Dir='http://130.206.112.29:1026/v2/entities/TL1/attrs/Direction/value'
UrlTL2Dir='http://130.206.112.29:1026/v2/entities/TL2/attrs/Direction/value'
UrlTL3Dir='http://130.206.112.29:1026/v2/entities/TL3/attrs/Direction/value'
UrlTL4Dir='http://130.206.112.29:1026/v2/entities/TL4/attrs/Direction/value'

UrlTL1L='http://130.206.112.29:1026/v2/entities/TL1/attrs/Light?type=TL'
UrlTL2L='http://130.206.112.29:1026/v2/entities/TL2/attrs/Light?type=TL'
UrlTL3L='http://130.206.112.29:1026/v2/entities/TL3/attrs/Light?type=TL'
UrlTL4L='http://130.206.112.29:1026/v2/entities/TL4/attrs/Light?type=TL'

UrlTL1Num='http://130.206.112.29:1026/v2/entities/TL1/attrs/NumCars/value'
UrlTL2Num='http://130.206.112.29:1026/v2/entities/TL2/attrs/NumCars/value'
UrlTL3Num='http://130.206.112.29:1026/v2/entities/TL3/attrs/NumCars/value'
UrlTL4Num='http://130.206.112.29:1026/v2/entities/TL4/attrs/NumCars/value'

headerTLDir = {'Fiware-Service': 'icai23944'
            }
headerTLL={'Fiware-Service': 'icai23944',
            'Fiware-ServicePath': '/environment/Cross1',
            'Content-type': 'application/json'
            }
payloadGreen={
    "value" : "1",
    "type": "bin"
}

payloadRed={
    "value" : "0",
    "type": "bin"
}


#
Dir=[0,0,0,0]
#inicializacion
print ('inicializacion')
r = requests.get(UrlTL1Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[0]=1
    p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[0]=2
    p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadRed))
r = requests.get(UrlTL2Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[1]=1
    p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[1]=2
    p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadRed))
r = requests.get(UrlTL3Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[2]=1
    p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[2]=2
    p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadRed))
r = requests.get(UrlTL4Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[3]=1
    p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[3]=2
    p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadRed))

# main Programe
print ('main')
start_time = time.time()
NumCar=[0,0,0,0]
Cycles=0
Temp1=30
Temp2=30
while 1:
    if Cycles % 2 == 0:
        while (time.time() - start_time) < Temp1:
            1
    else:
        while (time.time() - start_time) < Temp2:
            1
    start_time = time.time()
    r=requests.get(UrlTL1Num,headers=headerTLDir)
    c1=int(r.text[1:-1])
    NumCar[0]=NumCar[0]+c1
    print ('Semaforo 1 = '+str(c1))
    r = requests.get(UrlTL2Num, headers=headerTLDir)
    c2=int(r.text[1:-1])
    NumCar[1] =NumCar[1]+c2
    print ('Semaforo 2 = '+str(c2))
    r = requests.get(UrlTL3Num, headers=headerTLDir)
    c3=int(r.text[1:-1])
    NumCar[2] =NumCar[2]+c3
    print ('Semaforo 3 = '+str(c3))
    r = requests.get(UrlTL4Num, headers=headerTLDir)
    c4=int(r.text[1:-1])
    NumCar[3] =NumCar[3]+c4
    print ('Semaforo 4 = '+str(c4))
    if Cycles%2==0:
        if Dir[0]== 1:
            p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadGreen))
        if Dir[1]== 1:
            p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadGreen))
        if Dir[2]== 1:
            p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadGreen))
        if Dir[3]== 1:
            p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadGreen))
    else:
        if Dir[0]== 2:
            p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadGreen))
        if Dir[1]== 2:
            p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadGreen))
        if Dir[2]== 2:
            p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadGreen))
        if Dir[3]== 2:
            p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadRed))
        else:
            p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadGreen))
    Cycles = Cycles + 1
    print ("Duracion Dir 1 = "+str(Temp1))
    print ("Duracion Dir 2 = "+str(Temp2))
    print ('---------------------------')
    if Cycles>=4:
        print('Actualizando Tiempos...')
        NumCarDir1=(Dir[0]==1)*NumCar[0]+(Dir[1]==1)*NumCar[1]+(Dir[2]==1)*NumCar[2]+(Dir[3]==1)*NumCar[3]
        NumCarDir2 = (Dir[0] == 2) * NumCar[0] + (Dir[1] == 2) * NumCar[1] + (Dir[2] ==2)*NumCar[2]+(Dir[3] == 2)*NumCar[3]
        NumCarDir1=NumCarDir1
        NumCarDir2=NumCarDir2
        print ('Coches totales Dir 1 en estas ultimas 4 iter ='+ str(NumCarDir1))
        print ('Coches totales Dir 2 en estas ultimas 4 iter ='+ str(NumCarDir2))
        if NumCarDir1>NumCarDir2 and Temp2>=2:
            Temp1=Temp1+2
            Temp2=Temp2-2
        if NumCarDir2>NumCarDir1 and Temp1>=2:
            Temp1=Temp1-2
            Temp2=Temp2+2
        NumCar=[0,0,0,0]
        Cycles=0
        print ('---------------------------')
