# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:08 2018

@author: Arlo Eardley 1108472
"""
#Import the required libraries
import socket

#Set the port
serverPort = 7000

#Acquire the server IP address
serverIP = socket.gethostname()

#Create a UDP socket connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Allow the user to input a message for the server
message = raw_input("Message to server:")

#While the client has not ellected to quit
while message != 'q':
    
    #Send the message to the server
    clientSocket.sendto(message,(serverIP, serverPort))

    #Receive reply from the server
    ReceivedFromServer, serverAddress = clientSocket.recvfrom(1024)
    print("Server Reply:" + str(ReceivedFromServer))

    #Allow new message to be sent to the server
    message = raw_input("Message to server:")

#Send the quit message to the server
clientSocket.sendto(message,(serverIP, serverPort))

#Close the client socket
clientSocket.close()


