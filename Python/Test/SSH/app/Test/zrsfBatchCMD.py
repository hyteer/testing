# encoding:utf-8
################################################################
# SSH批量主机管理
# Version: 1.0
# Author: YT
################################################################
import paramiko, getpass, re, time
from datetime import datetime

now = str(datetime.now())
'''
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
'''
print u"请输入要管理的主机（用逗号隔开）："
hosts = raw_input('>')

print u"请输入Bash命令(多个命令用分号隔开)："
cmds = raw_input('>')

usr = "root"
passwd = "123456"
port = 22
openhosts = []
closedhosts = []
#oper = None

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

    print now, "\n" + u"执行主机： " + host + "..."
    #stdin, stdout, sterr = ssh.exec_command("cd /yt;pwd")
    #print stdout.read()
    #time.sleep(1)

    stdin, stdout, sterr = ssh.exec_command(cmds)
    channel = stdout.channel
    status = channel.recv_exit_status()
    print stdout.read()

    ssh.close()


def main():
    print "Start..."
    for host in hosts:
        ssh2(host,port,usr,passwd,cmds)

    print "All done..."


hosts = tsplit(hosts,(','))
print hosts

print u"输入yes开始执行"
fire = raw_input('>')
if fire=='yes':
    main()

