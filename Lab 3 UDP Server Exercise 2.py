# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:33:47 2018

@author: Arlo Eardley 1108472
"""

#Import the required libraries
import threading
import socket

#Define a class to handle the threads related to the client 
class Server(threading.Thread):

        #Over-ride the init fucntion to handle the threads
    def __init__(self,addr,data,server):
        
            threading.Thread.__init__(self)
            self.data = addr
            self.message = data
            self.server = server
        
        #Over-ride the rn function to handle the threads
    def run(self):
                

                    ClientMessage = (self.message).decode()
                    print ("The client has sent:  " + str(ClientMessage))
                    
                    #If the client has requested to quit
                    if ClientMessage == 'q':
                            print ("Client at " + str(self.data) + " has disconnected...")

                    #Otherwise continue communicating with the client
                    else:
                            print ("Server reply to client: " + str(self.data))

                            #Echo the message received from the client back to the client
                            self.server.sendto(ClientMessage,self.data)
                            
                    
# Define a main function to run the server                               
if __name__ == '__main__':
	
                #Set up the socket to use UDP 
		server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

                #Bind to the client on the port
		server.bind(('',7000))
		print ("UDP socket server is established")

		while True:
			
                        #Recieve information from the client
			data, addr = server.recvfrom(1024)

                        #Allocate a new thread to the client
			Clientthread = Server(addr,data,server)

                        #Start the thread for the new client
			Clientthread.start()
			

			
	



		
