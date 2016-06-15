# encoding: utf-8
#!/usr/bin/python
import paramiko

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
remotepath='/yt/jmeter-agent/startAgent.sh'
localpath='e:/Temp/ssh/startAgent.sh'

def upload(hosts):
    print "Begin to upload..."
    for host in hosts:
        t = paramiko.Transport((host,22))
        t.connect( username = usr, password = passwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put( localpath, remotepath)
        print "Upload to: " + host
        t.close()
    print "All done."
def download():
	t = paramiko.Transport(('10.10.16.47',22))
	t.connect( username = 'root', password = '123456')
	sftp = paramiko.SFTPClient.from_transport(t)
	sftp.get(remotepath, localpath)
	t.close()

#download()
upload(hosts)

