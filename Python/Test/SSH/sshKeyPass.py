# encoding: utf-8
#!c:/python27/scripts
import paramiko
import getpass

hostname='183.60.23.176'
username='manage'
pk_path='D:/TestShop/sshkey/YT-szdzfp.pem'
try:
        key=paramiko.RSAKey.from_private_key_file(pk_path)
except paramiko.PasswordRequiredException:
        password = getpass.getpass('admin@123')
        key = paramiko.RSAKey.from_private_key_file(pk_path, password)    # 需要口令的私钥
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
ssh.connect(hostname=hostname, username=username, pkey=key)
stdin, stdout, stderr=ssh.exec_command('pwd;ls')
# 下面的方法适合使用密码登陆的状况
# ssh.connect(hostname=hostname, username=username, password=‘123456’)
# stdin, stdout, stderr=ssh.exec_command('sudo su')
# stdin.write('123456')
# stdin.flush()

print stdout.read()
#print stdout.readlines()
#print stderr.readlines()
ssh.close()
