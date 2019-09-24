#!/usr/bin/python3

from subproces import getoutput
import sys

sum=0
data=sys.argv[1:]
for i in data :
    print("PING request for server: " =i)
    print(getoutput("ping - c 3 "+i))
    print("---------------------")
    print("---------------------")


    
