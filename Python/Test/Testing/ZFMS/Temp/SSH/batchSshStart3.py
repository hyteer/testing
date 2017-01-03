#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import time
#paramiko.util.log_to_file('/tmp/sshout')
serverlist = [
	{'ip':'10.10.16.47','usr':'root','passwd':'123456'},
	{'ip':'10.10.16.48','usr':'root','passwd':'123456'}

]
cmds = '''cd /yt/;ls;chmod -R 775 *;cd jmeter-agent;ls'''
cmds2 = [
    "cd /yt",
    "ls"
]
for host in serverlist:
    ip = host["ip"]
    usr = host["usr"]
    passwd = host["passwd"]
    s = serverlist
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,usr,passwd,timeout=5)
    print "CMD: cd /yt"
    stdin,stdout,stderr = ssh.exec_command("cd /yt/jmeter-agent;ls;./startAgent.sh &")
    print stdout.read()
    print '%s\tOK\n'%(ip)
    ssh.close()


#ssh2("10.10.16.41","root","123456","hostname;cd /yt;ls")
#ssh2("10.10.16.42","root","123456","hostname;cd /yt;mkdir test;ls")