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
# enter message
while True:
    msg=input("Enter data to send:")    
# converting data into byte-like string format
    newmsg=msg.encode('ascii')
# lets send data to target
    s.sendto(newmsg,("127.0.0.1",8899))
    data=s.recvfrom(10000)
    print(data)
