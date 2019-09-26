#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko

# multivendor library

device1={
	'username' : 'root',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '192.168.54.128'
}


# to connect to target device
#by checking of couple of things connect handler will allow you to connect
'''
       device_type
'''

device_connect=netmiko.ConnectHandler(**device1)
print(device_connect) 
print([i for i in dir(device_connect) if 'send' in i])

#now sending command

cmd=["show ip int br", "show ippp"]

for i in cmd:
	print("Sending command ", i)
	print("----------------")
	output=device_connect.send_command(i)
	print(output)


