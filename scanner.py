#!/bin/python3
import sys
import socket
from datetime import datetime
a = input("Enter IP address")
x = int(input("Enter starting port"))
y = int(input("Enter ending port"))
if len(a) == 2:
    target = socket.gethostbyname(a[1])

print("-" * 50)
print("scanner target " + a)
print("time standard: " + str(datetime.now()))
print("-" * 50)

for port in range(x,y):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = s.connect_ex((a,port))
	print("checking port{}".format(port))
	if result == 0:
		print("port {} is oprn".format(port))
	s.close()
