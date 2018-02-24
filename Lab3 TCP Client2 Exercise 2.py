# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:23:23 2018

@author: Arlo
"""

# Python TCP Client B
import socket 

host = socket.gethostname() 
port = 2004 
MESSAGE = raw_input("Message from client 2:")
 
Client2TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Client2TCP.connect((host, port))

while MESSAGE != 'q':
    Client2TCP.send(MESSAGE)     
    data = Client2TCP.recv(4096)
    print("Server Reply: " + data)
    MESSAGE = raw_input("Message from client 2:")
Client2TCP.send(MESSAGE)
Client2TCP.close() 