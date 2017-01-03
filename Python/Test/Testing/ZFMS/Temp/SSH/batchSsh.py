#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import time
#paramiko.util.log_to_file('/tmp/sshout')
serverlist = [
	{'ip':'10.10.16.47','usr':'root','passwd':'123456'},
	{'ip':'10.10.16.48','usr':'root','passwd':'123456'}

]
cmds = [
    "cd /yt",
    "chmod -R 775 jmeter-agent jre1.8",
    "cd jmeter-agent",
    "./startAgent.sh &"
]
cmds2 = "cd /yt;ls;chmod -R 775 jmeter-agent jre1.8"
cmds3 = [
    {"cmd": "cd /yt"},
    {"cmd": "chmod -R 777 temp"},
]
cmds4 = [
    "cd /yt",
    "chmod -R 777 temp"
]

s = serverlist
def ssh2(ip,username,passwd,cmd):

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
#           stdin.write("Y")   #简单交互，输入 ‘Y’
        print stdout.read()
#        for x in  stdout.readlines():
#          print x.strip("\n")
        print '%s\tOK\n'%(ip)

        ssh.close()

    except :
        print '%s\tError\n'%(ip)
    print "--全部完成--"

#print "Server #1's IP: " + serverlist[0]['ip']

for host in serverlist:
    ip = host["ip"]
    usr = host["usr"]
    passwd = host["passwd"]
    #print ip+" "+usr+" "+passwd
    #ssh2(ip,usr,passwd,"hostname;cd /yt;ls")
    ssh2(ip,usr,passwd,cmds3)
    time.sleep(2)


#ssh2("10.10.16.41","root","123456","hostname;cd /yt;ls")
#ssh2("10.10.16.42","root","123456","hostname;cd /yt;mkdir test;ls")