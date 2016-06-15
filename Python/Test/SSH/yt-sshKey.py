#!/usr/bin/env python
import paramiko

hostname='52.221.243.152'
port=22
username='ubuntu'
pkey='D:/TestShop/sshkey/YT_AWS_Sigapore.pem'


key=paramiko.RSAKey.from_private_key_file(pkey)

s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.load_system_host_keys()
s.connect(hostname,port,username,pkey=key)
stdin,stdout,stderr=s.exec_command('hostname;ls')

print stdout.read()