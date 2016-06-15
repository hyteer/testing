# encoding: utf-8
import time
import thread
import paramiko
from datetime import datetime

# --------------initial all constants and variables-------------

#cmds = "hostname;pwd"
usr = "root"
passwd = "123456"
port = 22
openhosts = []
closedhosts = []
flag = ''
cmds = ''
hosts = []
'''
hosts = [
    '10.10.16.41',
    '10.10.16.42',
    '10.10.16.43',
    '10.10.16.44',
]
'''

# -----------------------Method definitions----------------------
def now():
    now = str(datetime.now())
    return now

def timer(no, interval):
    cnt = 0
    while cnt<3:
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())
        time.sleep(interval)
        cnt+=1
    thread.exit_thread()

def tsplit(string, delimiters):
    """Behaves str.split but supports multiple delimiters."""

    delimiters = tuple(delimiters)
    stack = [string,]

    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)

    return stack


def ssh2(host,port,usr,passwd,cmds):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, usr, passwd, timeout = 8)

    #print now(), "\n" + u"执行主机： " + host + "..."
    #stdin, stdout, sterr = ssh.exec_command("cd /yt;pwd")
    #print stdout.read()
    #time.sleep(1)

    stdin, stdout, sterr = ssh.exec_command(cmds)
    channel = stdout.channel
    status = channel.recv_exit_status()

    print "主机：" + host + "\n" +stdout.read()

    ssh.close()

def main ():
    for host in hosts:

        try:
            thread.start_new_thread(ssh2,(host,port,usr,passwd,cmds))
        except:
            print "Error: unable to start thread"
            print "All done..."

# ---------------------------Call main()-------------------------

print u"请输入要管理的主机（用逗号隔开）："
hosts = raw_input('>')
print u"请输入Bash命令,回车执行(多个命令用分号隔开)："
cmds = raw_input('>')
hosts = tsplit(hosts,(','))
#print hosts
main()

while 1:
    pass


'''
if __name__=='__main__':
    test()
'''