# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:21:31 2018

@author: Arlo Eardley 1108472
"""

import socket 

#acquire the name of the server hosting the connection
host = socket.gethostname() 

#set the port to operate on 
port = 2004

#Send the initial message to the server
MESSAGE = raw_input("Message from client 1:") 

#Create a TCP socket
ClientTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Connect to the server
ClientTCP.connect((host, port))

#While the client has not elected to quit
while MESSAGE != 'q':
    
    #Send message to the server
    ClientTCP.send(MESSAGE) 

    #Receive the reply form the server    
    data = ClientTCP.recv(4096)

    #Print out the reply from the server
    print("Server Reply: " + data)

    #Input a new message to reply to thh server
    MESSAGE = raw_input("Message from client 1:")

#Send the last message to server to lt it know client has quit
ClientTCP.send(MESSAGE)

#Close the client TCP connection
ClientTCP.close()