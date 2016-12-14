#coding:utf-8
import os
import socket
import subprocess
HOST = '0.0.0.0'               
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        command = conn.recv(1024)
        print command
    if not command:
        break
        if command == 'quit':
            break
        #data = os.popen(command).read()
    res = "hi,message received"
    #result = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = result.stdout.read()
    conn.sendall(res)
    conn.close()
s.close()