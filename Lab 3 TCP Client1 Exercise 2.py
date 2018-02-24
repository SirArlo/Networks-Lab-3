# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:21:31 2018

@author: Arlo
"""

# Python TCP Client A
import socket 

host = socket.gethostname() 
port = 2004
MESSAGE = raw_input("Message from client 1:") 
 
Client1TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Client1TCP.connect((host, port))

while MESSAGE != 'q':
    
    Client1TCP.send(MESSAGE)     
    data = Client1TCP.recv(4096)
    print("Server Reply: " + data)
    MESSAGE = raw_input("Message from client 1:")

Client1TCP.send(MESSAGE)
Client1TCP.close()