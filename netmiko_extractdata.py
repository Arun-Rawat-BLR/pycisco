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
output=device_connect.send_command("show ip int br", use_textfsm=True)
print(output)


