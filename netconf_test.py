#!/user/bin/python3

import time
from ncclient import manager

# this code will act as netconf client

# using connect function with manager to connect Netconf enabled device
device=manager.connect(host='192.168.54.128',username='root',password='cisco',port=22,allow_agent=False,look_for_keys=False,hostkey_verify=False)
print(device)
print("_____________________________")
print("_____________________________")
time.sleep(2)
print(dir(device))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
time.sleep(1)
print(device.get_config('running').data.xml)
