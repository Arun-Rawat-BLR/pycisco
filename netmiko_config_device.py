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

#now sending configuration for devices
conf=["hostname pyrouter1", "username hello privi 10 password cisco"]
output=device_connect.send_config_set(conf)
print(output)
# sending configuration from file
output1=device_connect.send_config_from_file('test_config.txt')
print(output1)

