# -*- coding:utf-8 -*-
#

from socket import *
from time import ctime
import random

HOST = '0.0.0.0'
PORT = 11111
BUFSIZE=1024
ADDR=(HOST, PORT)

tcpSrvSock=socket(AF_INET, SOCK_STREAM)
tcpSrvSock.bind(ADDR)
tcpSrvSock.listen(5)

while True:
	
	print 'waiting for connection ...'
	tcpCliSock,addr = tcpSrvSock.accept()
	print '... connected from:', addr

	while True:
		randnum = str(random.randint(10,99))
		data=tcpCliSock.recv(1024)
		if not data:
			break
		tcpCliSock.send('[%s], RandomNum:%s'%(ctime(), randnum))
		print [ctime()],':',data


tcpCliSock.close()