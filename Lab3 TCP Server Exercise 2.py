# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:23:23 2018

@author: Arlo Eardley 1108472
"""

#Import the required libraries
import socket, threading


#Create a class to handle the client threads
class ClientThread(threading.Thread):
    
    #Initialise the client threads
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection request from: " + str(clientAddress))

    #Overide the run fuction to perform client threading   
    def run(self):

        print ("Connected to : " + str(clientAddress))
        reply = ''

        while True:

            #Echo back to client whatever the server has received
            reply = (self.csocket.recv(2048)).decode()

            #If the reply was to quit then stop communication with that client
            if reply=='q':
              break
            print ("Message from client: " + str(clientAddress) + " " +  str(reply))
            self.csocket.send(reply)
        print ("Client at " + str(clientAddress) + " has disconnected...")

# Initialise the Host and port      
LOCALHOST = "0.0.0.0"
PORT = 2004

#Create the TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Allow the re-use of an address
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind to the client port
server.bind((LOCALHOST, PORT))


print("Server has started")
print("Awaiting client connection request..")

#While the client is still connected to the server
while True:

    #Listen for connections
    server.listen(1)

    #Accept the client requests
    clientsock, clientAddress = server.accept()

    #allocate a new thread to the client that has sent the request
    newthread = ClientThread(clientAddress, clientsock)

    #Start the new thread for that client
    newthread.start()
