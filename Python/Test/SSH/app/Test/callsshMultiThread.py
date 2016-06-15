# encoding: utf-8
import time
import thread
import paramiko
import threading,thread
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

exitFlag = 0

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

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, delay, flag):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.flag = flag
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        print_time(self.name, self.delay, self.flag)
        #print "Exiting " + self.name
        #thread.exit_thread()

def print_time(threadName, delay, flag):
    global exitFlag
    print "%s: %s" % (threadName, time.ctime(time.time()))

class ssh2Thread(threading.Thread):
    def __init__(self, host,port,usr,passwd,cmds):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.usr = usr
        self.passwd = passwd
        self.cmds = cmds
    def run(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, self.port, self.usr, self.passwd, timeout = 8)

        #print now(), "\n" + u"执行主机： " + host + "..."
        #stdin, stdout, sterr = ssh.exec_command("cd /yt;pwd")
        #print stdout.read()
        #time.sleep(1)

        stdin, stdout, sterr = ssh.exec_command(cmds)
        channel = stdout.channel
        status = channel.recv_exit_status()

        print "主机：" + self.host + "\n" +stdout.read()

        ssh.close()


# 创建新线程
sshthreads = []
delay = 1
print u"请输入要管理的主机（用逗号隔开）："
hosts = raw_input('>')
print u"请输入Bash命令,回车执行(多个命令用分号隔开)："
cmds = raw_input('>')
hosts = tsplit(hosts,(','))


print "Please input 'start' to start:"
flag = raw_input('>')
if flag == 'start':
    for host in hosts:
        sshthreads.append( ssh2Thread(host,port,usr,passwd,cmds))
        #thread2 = myThread(2, "Thread-2", delay, flag)
        #thread3 = myThread(3, "Thread-3", delay, flag)


# 开启线程

for sshthread in sshthreads:
        sshthread.start()
        #thread1.start()
        #thread2.start()
        #thread3.start()


print "Exiting Main Thread"