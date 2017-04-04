import requests
import json
import time

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

headerTLDir = {'Fiware-Service': 'icai23944',
            'Fiware-ServicePath': '/environment/Cross1'
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

Dir=[0,0,0,0]
#inicializacion
r = requests.get(UrlTL1Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[0]=1
    p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[0]=2
    p = requests.put(UrlTL1L, headers=headerTLL, json=(payloadRed))
print p.json()
r = requests.get(UrlTL2Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[1]=1
    p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[1]=2
    p = requests.put(UrlTL2L, headers=headerTLL, json=(payloadRed))
print p.json()
r = requests.get(UrlTL3Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[2]=1
    p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[2]=2
    p = requests.put(UrlTL3L, headers=headerTLL, json=(payloadRed))
print p.json()
r = requests.get(UrlTL4Dir,headers=headerTLDir)
if r.json()=='N' or r.json()=='S':
    Dir[3]=1
    p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadGreen))
else:
    Dir[3]=2
    p = requests.put(UrlTL4L, headers=headerTLL, json=(payloadRed))
print p.json()

start_time = time.time()
NumCar=[0,0,0,0]
Cycles=0
Temp1=30
Temp2=30
while 1:
    if Cycles%2==0:
        while (time.time() - start_time) < Temp1:
            1
    else:
        while (time.time() - start_time) < Temp2:
            1
    start_time = time.time()
    r=requests.get(UrlTL1Num,headers=headerTLDir)
    NumCar[0]=NumCar[0]+int(r.text[1])
    r = requests.get(UrlTL2Num, headers=headerTLDir)
    NumCar[1] =NumCar[1]+int(r.text[1])
    r = requests.get(UrlTL3Num, headers=headerTLDir)
    NumCar[2] =NumCar[2]+int(r.text[1])
    r = requests.get(UrlTL4Num, headers=headerTLDir)
    NumCar[3] =NumCar[3]+int(r.text[1])
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
    print NumCar
    Cycles = Cycles + 1
    print Temp1
    print Temp2
    if Cycles==4:
        NumCarDir1=(Dir[0]==1)*NumCar[0]+(Dir[1]==1)*NumCar[1]+(Dir[2]==1)*NumCar[2]+(Dir[3]==1)*NumCar[3]
        NumCarDir2 = (Dir[0] == 2) * NumCar[0] + (Dir[1] == 2) * NumCar[1] + (Dir[2] ==2)*NumCar[2]+(Dir[3] == 2)*NumCar[3]
        NumCarDir1=NumCarDir1/4.0
        NumCarDir2=NumCarDir2/4.0
        print NumCarDir1
        print NumCarDir2
        if NumCarDir1>NumCarDir2 and Temp2>=24:
            Temp1=Temp1+2
            Temp2=Temp2-2
        if NumCarDir2>NumCarDir1 and Temp1>=24:
            Temp1=Temp1-2
            Temp2=Temp2+2
        NumCar=[0,0,0,0]
        Cycles=0