# -*- coding:utf-8 -*-
#

from socket import *

def start_client():
	HOST='localhost'
	PORT=11111
	BUFSIZE=1024
	ADDR=(HOST, PORT)

	tcpCliSock=socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)

	while True:
		data = raw_input('>')
		if not data:
			break
		tcpCliSock.send(data)
		data=tcpCliSock.recv(BUFSIZE)
		if not data:
			break
		print data

	tcpCliSock.close()


start_client()