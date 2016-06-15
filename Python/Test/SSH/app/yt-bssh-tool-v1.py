#!/usr/bin/env python
# encoding: utf-8
################################################################
# SSH远程批量管理工具
# Version: 1.0
# Author: YT
# 注：upinfo和download的返回值都为(localpath,remotepath,uptype)
################################################################
import paramiko
import time
from datetime import datetime

def now():
    now = str(datetime.now())
    return now

host='52.221.243.152'
port=22
user='ubuntu'
pkey='D:/TestShop/sshkey/YT_AWS_Sigapore.pem'
#remotepath='/home/ubuntu/temp/startAgent.sh'
#localpath='d:/Temp/ssh/tmp/startAgent.sh'

key=paramiko.RSAKey.from_private_key_file(pkey)

'''
s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.load_system_host_keys()
s.connect(host,port,user,pkey=key)
stdin,stdout,stderr=s.exec_command('hostname;ls')

print stdout.read()
'''
# -----------------定义操作函数---------------
def upLoad(upinfo):
    localpath,remotepath,uptype = upinfo
    print u"确认上传？(yes/no)"
    confirm = raw_input(">")
    print u"开始上传..."
    t = paramiko.Transport(host,port)
    t.connect(username=user, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(localpath,remotepath)
    print u"上传完成"

def downLoad(localpath,remotepath):
    print u"确认下载？(yes/no)"
    confirm = raw_input(">")
    print u"开始下载..."
    t = paramiko.Transport(host,port)
    t.connect(username=user, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remotepath, localpath)
    print u"下载完成"

def runCmd(host,port,usr,passwd,oper):
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
print u"\
##############################\n\
# SSH远程批量管理工具\n\
# Version: 1.0\n\
# Author: YT\n\
##############################"
def getInput():
    print u"请选择操作：\n1.上传文件\n2.下载文件\n3.执行命令"
    type = None
    upinfo = None
    downinfo = None
    localpath = None
    remotepath = None

    def getUpInfo():
        print u"请选择上传类型（输入数字）："
        print u"1.上传单个文件\n2.批量上传"
        uptype = None
        while (uptype != "1" and uptype !="2"):
            uptype = raw_input(">")

            if uptype =="1":
                print u"请输入本地文件完整路径："
                localpath=raw_input('>')
                print u"请输入远程路径及文件名："
                remotepath=raw_input('>')
            elif uptype =="2":  # 批量上传功能暂未完成。。。
                print u"请输入本地上传目录："
                localpath=raw_input('>')
                print u"请输入远程路径："
                remotepath=raw_input('>')
            else:
                print u"请重新输入："

        return localpath, remotepath,uptype

    def getDownInfo():
        print u"请选择下载类型（输入数字）："
        print u"1.下载单个文件\n2.批量下载"
        downtype = None
        while (downtype != "1" and downtype !="2"):

            downtype = raw_input("Type a Number:")
            if downtype =="1":
                print u"请输入远程路径及文件名："
                remotepath=raw_input('>')
                print u"请输本地存放路径："
                localpath=raw_input('>')
            elif downtype =="2":  # 批量下载功能暂未完成。。。
                print u"请输入远程下载目录："
                remotepath=raw_input('>')
                print u"请输入本地存放路径："
                localpath=raw_input('>')
            else:
                print u"输入有误，请重新输入"

        return localpath, remotepath,downtype

    def getCmdInfo():
        print u"请输入主机IP："
        # 请功能暂未完成。。。


    while (type != "1" and type !="2" and type!="3"):

        type = raw_input(">")
        #type=input(">")
        if type=="1":
            upinfo=getUpInfo()
        elif type=="2":
            downinfo=getDownInfo()
        elif type=="3":
            cmdInfo=getCmdInfo()
        else:
            print u"输入有误，请重新输入"
    inputinfo = dict(type=type,upinfo=upinfo,downinfo=downinfo)

    return inputinfo




# -------------------定义主函数------------------
def main():
    inputinfo=getInput()
    type = inputinfo['type']
    upinfo = inputinfo['upinfo']
    downinfo = inputinfo['downinfo']
    #cmdinfo = inputinfo['cmdinfo']
    #print "Info: ",inputinfo
    #print "UpInfo: ",upinfo
    #print "DownInfo: ",downinfo
    if type=="1":
        upLoad(upinfo)
    elif type=="2":
        downLoad(downinfo)
    elif type=="3":
        print u"还未实现此功能"
    else:
        print u"未知错误"

main()






