# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:33:47 2018

@author: Arlo
"""

import threading
import socket


class Server(threading.Thread):

	
    def __init__(self,addr,data,server):
        
            threading.Thread.__init__(self)
            self.data = addr
            self.message = data
            self.server = server
        
    def run(self):

                    #print ("Serving the current client: " + str(self.data) )
                    ClientMessage = (self.message).decode()
                    print ("The client has sent:  " + str(ClientMessage))
                    
                    if ClientMessage == 'q':
                            print ("Client at " + str(self.data) + " has disconnected...")
                            
                    else:
                            print ("Server reply to client: " + str(self.data))
                            self.server.sendto(ClientMessage,self.data)
                            
                    
                                      
if __name__ == '__main__':
	

		server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		server.bind(('',7000))
		print ("UDP socket server is established")

		while True:
			
			data, addr = server.recvfrom(1024)
			Clientthread = Server(addr,data,server)
			Clientthread.start()
			

			
	



		
