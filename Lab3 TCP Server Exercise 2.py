# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:23:23 2018

@author: Arlo
"""

 
import socket, threading

class ClientThread(threading.Thread):
    
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection request from: " + str(clientAddress))
        
    def run(self):
        print ("Connected to : " + str(clientAddress))
        reply = ''
        while True:
            reply = (self.csocket.recv(2048)).decode()
            #reply = data.decode()
            if reply=='q':
              break
            print ("Message from client: " + str(clientAddress) + " " +  str(reply))
            self.csocket.send(reply)
        print ("Client at " + str(clientAddress) + " has disconnected...")
        
LOCALHOST = "0.0.0.0"
PORT = 2004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server has started")
print("Awaiting client connection request..")

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
