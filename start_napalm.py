#!/usr/bin/python3

from napalm import get_network_driver
driver=get_network_driver('ios')
# connecting to device
device=driver('192.168.54.128','root','cisco')

print([i for i in dir(device) if 'load' in i])
# open session with device
device.open()
# merging configuration
print(device.load_merge_candidate(filename='/Users/arrawat/pycisco/test_config.txt'))
#check the difference
print(device.compare_config())
# now to commit the applied configuration
c=input("Confirm with y|n to apply configuration")

if c == 'y' or c == 'Y' :
	print("Committing the configuration")
	device.commit_config()
elif c == 'n' or c == 'N':
	print("discarding configration")
	device.discard_config()
else :
	print("Please typle only y or n")

