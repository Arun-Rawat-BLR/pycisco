#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko

# multivendor library

from getpass import getpass
sec1=getpass("Pls enter password for device1:")
#accept passowrd without showing on screen


device1={
	'username' : 'root',
	'password' : sec1,
	'device_type' : 'cisco_ios',
	'host' : '192.168.54.128'
}

sec2=getpass("Pls enter password for device2:")
device2={
	'username' : 'root',
	'password' : sec2,
	'device_type' : 'cisco_ios',
	'host' : '192.168.202.131'
}


for i in [device1,device2] :
	try :
		#sec=getpass("Pls enter password for decvice")
		print("connecting with Device type :-->", i['device_type']," Having IP", i ['host'])
		print("-------------------------")
		print("-------------------------")
		device_connect=netmiko.ConnectHandler(**i)
		#sending command
		output=device_connect.send_command("show ip int br")
		print(output)
		print("-------------------------")
		print("-------------------------")
	except netmiko.ssh_exception.NetMikoTimeoutException :
		print("Please check your IP or network:", i['host'])
	except netmiko.ssh_exception.NetMikoAuthentcationException :
		print("Please check your authentication details for device:", i['host'])
	except ValueError :
		print("Please check device type or values in Host", i['host'])


