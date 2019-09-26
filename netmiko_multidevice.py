#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko

# multivendor library

device1={
	'username' : 'root',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '192.168.54.128'
}

device2={
	'username' : 'root',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '192.168.202.131'
}


for i in [device1,device2] :
	print("connecting with Device type :-->", i['device_type']," Having IP", i ['host'])
	print("-------------------------")
	print("-------------------------")
	device_connect=netmiko.ConnectHandler(**i)
	#sending command
	output=device_connect.send_command("show ip int br")
	print(output)
	print("-------------------------")
	print("-------------------------")




