# -*- coding:utf-8 -*-



if __name__=="__main__":  
		import sys
		import socket  
		host = sys.argv[1]
		port = int(sys.argv[2])

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
		sock.connect((host, port))    
		import time    
		str = "client str" 
		while True: 
				#data = raw_input('>')  
		        time.sleep(3)    
		        print 'send to server with value: '+ str   
		        sock.send(str)    
		        print sock.recv(1024)   
		        
		          
		sock.close() 


