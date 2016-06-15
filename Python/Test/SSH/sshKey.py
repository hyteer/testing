#!/usr/bin/env python
import paramiko

hostname='183.60.23.176'
port=22
username='manage'
pkey='D:/TestShop/sshkey/yt_zrsfnewdt_nopass.pem'


key=paramiko.RSAKey.from_private_key_file(pkey)

s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.load_system_host_keys()
s.connect(hostname,port,username,pkey=key)
stdin,stdout,stderr=s.exec_command('hostname;ls')

print stdout.read()