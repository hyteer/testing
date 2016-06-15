import paramiko, getpass, re, time
from datetime import datetime

now = str(datetime.now())

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

print now, "before call"
#stdin, stdout, sterr = ssh.exec_command("ls")
#print stdout.read()
#time.sleep(2)
stdin, stdout, sterr = ssh.exec_command("sleep 5")
print now, "now just run some other commands..."
stdin, stdout, sterr = ssh.exec_command("ls")
print stdout.read()
print now, "after call"
channel = stdout.channel
print now, "before status"

status = channel.recv_exit_status()


print now, "after status"