# -*- coding:utf-8 -*-


if __name__=="__main__":  

		import socket    
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
		sock.connect(('localhost', 11111))    
		import time    
		str = "client str" 
		while True: 
				#data = raw_input('>')  
		        time.sleep(3)    
		        print 'send to server with value: '+ str   
		        sock.send(str)    
		        print sock.recv(1024)   
		        
		          
		sock.close() 


