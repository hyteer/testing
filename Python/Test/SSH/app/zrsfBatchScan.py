import paramiko, getpass, re, time
from datetime import datetime

now = str(datetime.now())

hosts = [
    '10.10.16.41',
    '10.10.16.42',
    '10.10.16.43',
    '10.10.16.44',
    '10.10.16.45',
    '10.10.16.46',
    '10.10.16.47',
    '10.10.16.48',
    '10.10.16.49',
    '10.10.16.50',
    '10.10.16.51',
    '10.10.16.52',
    '10.10.16.53',
    '10.10.16.54',
    '10.10.16.55',
    '10.10.16.56',
    '10.10.16.57',
    '10.10.16.58'

]
usr = "root"
passwd = "123456"
port = 22
cmd = None
#oper = None

def ssh2(host,port,usr,passwd,oper):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, usr, passwd, timeout = 8)

    print now, "Logined,begin to do..."
    stdin, stdout, sterr = ssh.exec_command("cd /yt;pwd")
    print stdout.read()
    time.sleep(1)

    stdin, stdout, sterr = ssh.exec_command('''nmap -p4444 127.0.0.1''')

    #print now, "after operation...."
    channel = stdout.channel
    #print now, "before status back..."
    status = channel.recv_exit_status()
    #print now, "after status back..."

    #stdin, stdout, sterr = ssh.exec_command("ls")
    print stdout.read()
    print  host + " Done."

    ssh.close()

print "Start..."
for host in hosts:
    ssh2(host,port,usr,passwd,cmd)

print "Finished..."

