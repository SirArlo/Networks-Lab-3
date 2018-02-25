# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:08 2018

@author: eards
"""

import socket
serverPort = 7000
serverIP = socket.gethostname()

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input("Message to server:")
while message != 'q':
    
    clientSocket.sendto(message,(serverIP, serverPort))
    ReceivedFromServer, serverAddress = clientSocket.recvfrom(1024)
    print("Server Reply:" + str(ReceivedFromServer))
    message = raw_input("Message to server:")

clientSocket.sendto(message,(serverIP, serverPort))
clientSocket.close()


