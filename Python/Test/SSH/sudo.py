import paramiko, getpass, re, time

serverlist = [
	{'ip':'192.168.198.128','usr':'tony','passwd':'sa'},
	{'ip':'10.10.16.48','usr':'root','passwd':'123456'}

]
s = serverlist

ip = s[0]["ip"]
usr = s[0]["usr"]
passwd = s[0]["passwd"]


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,22,usr,passwd,timeout=5)
print "Begin to run job on: " + ip
'''
stdin,stdout,stderr = ssh.exec_command("cd test/tmp/jmeter-agent;ls", timeout=5)
print stdout.read()

'''

channel = ssh.invoke_shell()
channel.send( "cd test/tmp/jmeter-agent" )
channel.recv(1024)
#wait for prompt
#while not re.search(".*\[sudo\].*",channel.recv(1024)): time.sleep(1)
channel.send( "ls" )
#print stdout.read()

print '%s\tOK\n'%(ip)
ssh.close()