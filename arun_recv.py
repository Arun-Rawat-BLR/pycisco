#!/usr/bin/python3

import socket,time
# checking for socket functions

print([i for i in dir(socket) if 'socket' in i])

#  now creating UDP socket
# ipv4 socket ---- ipv4 + 2 byte port
# ipv6 socket ---  ipv6 + 2 byte port
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # for IPV4 UDP socket
#socket.socket(scoket.AF_INET,SOCK_STREAM) # for TCP

#####

s.bind(("",8895)) # if IP is not assigned, 0.0.0.0 is default

# bind will accept tuple format IP & Port
while True :
    data=s.recvfrom(1000) # this is buffer size
    print(data[0])
    print("Sender address is ", data[1])
    msg=input("enter reply: ")
    newmsg=msg.encode('ascii')
    s.sendto(newmsg,data[1])
