# encoding: utf-8
from multiprocessing import Process
import os
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
choice = ''

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name


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
def home():
    global choice
    global flag
    print u"请选择操作：\n1.执行命令\n2.上传文件\n3.下载文件\n输入'exit'退出"
    choice = raw_input('>')
    setChoice(choice)
    while choice != '1' and choice != 'exit':
        print u"请选择操作：\n1.执行命令\n2.上传文件\n3.下载文件\n输入'exit'退出"
        print "Please choose from the menu."
        choice = raw_input('>')
        setChoice(choice)
        #print "choice:",choice
    setFlag('nemo')

def starter():
    global hosts
    global cmds
    print u"请输入要管理的主机（用逗号隔开）："
    hosts = raw_input('>')
    print u"请输入Bash命令,回车执行(多个命令用分号隔开)："
    cmds = raw_input('>')
    hosts = tsplit(hosts,(','))
#print hosts

def setFlag(flg):
    global flag
    flag = flg

def setChoice(chs):
    global choice
    choice = chs

'''
if __name__=='__main__':
    test()
'''

#host = "10.10.16.22"


if __name__ == '__main__':
    #starter()
    #global choice
    #global flag
    home()

    while flag != 'exit':
        #info('main line')
        #print "Choice: ",choice
        #print "Flag:",flag
        if flag == 'home':
            home()
        if choice == '1':
            starter()
        elif choice == 'exit':
            setFlag('exit')
        elif choice != 'nemo':
            setFlag('home')
            print "Please choose from below."

        if flag != 'exit' and flag != 'home':
            print u"开始执行..."
            #p = Process(target=f, args=('bob',))
            for host in hosts:
                #ssh2(host,port,usr,passwd,cmds)
                try:
                    #thread.start_new_thread(ssh2,(host,port,usr,passwd,cmds))
                    #p=Process(target=ssh2,args=(host,port,usr,passwd,cmds))
                    #p.start()
                    #p.join()
                    ssh2(host,port,usr,passwd,cmds)
                except:
                    print "Error: unable to start thread"
                    print "All done..."

            time.sleep(0.3)
            print u"请继续输入命令：\n(输入exit退出,输入home回到主菜单)"
            cmds = raw_input('bash>')
            if cmds == 'exit' or cmds == 'home':
                flag = cmds

        choice = 'nemo'



