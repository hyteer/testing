#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import time
#paramiko.util.log_to_file('/tmp/sshout')
serverlist = [
	{'ip':'192.168.198.128','usr':'tony','passwd':'sa'},
	{'ip':'10.10.16.48','usr':'root','passwd':'123456'}

]
s = serverlist
cmds = '''cd /yt/;ls;chmod -R 775 *;cd jmeter-agent;ls'''
cmds2 = [
    "cd /yt",
    "ls"
]

ip = s[0]["ip"]
usr = s[0]["usr"]
passwd = s[0]["passwd"]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,22,usr,passwd,timeout=5)
print "Begin to run job on: " + ip
stdin,stdout,stderr = ssh.exec_command("cd test/tmp/jmeter-agent;./startAgent.sh &;ls", timeout=5)
print stdout.read()
print '%s\tOK\n'%(ip)
ssh.close()


#ssh2("10.10.16.41","root","123456","hostname;cd /yt;ls")
#ssh2("10.10.16.42","root","123456","hostname;cd /yt;mkdir test;ls")