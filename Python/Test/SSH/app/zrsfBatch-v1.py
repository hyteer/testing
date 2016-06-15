import paramiko, getpass, re, time
from datetime import datetime

def now():
    now = str(datetime.now())
    return now

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
#oper = None

def ssh_agent(host,port,usr,passwd,oper):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, usr, passwd, timeout = 8)

    print now(), "\nLogin to: " + host
    stdin, stdout, sterr = ssh.exec_command("cd /yt; chmod -R 755 *; pwd")
    print stdout.read()
    time.sleep(1)

    if oper == 'kill':
        stdin, stdout, sterr = ssh.exec_command('''kill -9 `ps -aux |grep "PerfMonAgent"| awk '{print $2}'`''')
        channel = stdout.channel
        status = channel.recv_exit_status()
        print stdout.read()
        print now(),"Killed..."
    elif oper == 'start':
        stdin, stdout, sterr = ssh.exec_command("/yt/jmeter-agent/startAgent.sh &")
        channel = stdout.channel
        status = channel.recv_exit_status()
        print stdout.read()
        print now(),"Started..."

    #print now, "after operation...."
    #channel = stdout.channel
    #print now, "before status back..."
    #status = channel.recv_exit_status()
    #print now, "after status back..."
    #print stdout.read()

    print  now() ,+ host + " done.\n\n"

    ssh.close()


print "Start..."

for host in hosts:
    ssh_agent(host,port,usr,passwd,"start")

print "Finished..."

