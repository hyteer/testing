# encoding: utf-8
#!/usr/bin/python
import paramiko

t = paramiko.Transport('192.168.198.128','22')
t.connect(username = 'tony', password = 'sa')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/home/tony/test/tmp/jmeter-agent/startAgent.sh'
localpath='d:/Temp/ssh/tmp/startAgent.sh'
sftp.get(remotepath, localpath)
#sftp.put('d:/Temp/ssh/testSFTP.txt','/yt/tmp/sftpTest.txt')
t.close()