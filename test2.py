#!/usr/bin/python3

'''
x=input("Enter number:")
print(x)
'''
from time import sleep
import sys

sum=0
data=sys.argv[1:]
for i in data :
    sum=sum+int(i)

print(sum)
    
