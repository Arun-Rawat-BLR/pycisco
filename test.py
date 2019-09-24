#!/usr/bin/python3

from time import ctime,sleep
#only importing desired functions
from subprocess import getstatusoutput,getoutput
from os import mkdir

options='''
press 1 to check current data and time:
Press 2 to run any command in your current OS:
Press 3 to create a directory:
Press 4 to start a train:
Press 5 Ping any website:    
'''
print (options)
# to capture input from user
choice=input()
print("you have chossen ", choice)
# conditional sttament with if
if choice == '1':
    print(ctime())
elif choice=='2':
    cmd=input("Pls enter any command:")
    output=getoutput(cmd)
    print(output)
elif int(choice) == 3:
    d_name=input("Enter directory name to create:")
    mkdir(d_name)
    List_Dir=ls
while (d_name in List_Dir == True) :
    print("Directory alreay exists. Create another name")
    print(d_name,"successfully created")
elif choice == '5':
    web=input("enter website name to ping:")
    print(getoutput("ping -c 5"+web)
else :
    print("wrong option")
    
