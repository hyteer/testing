import urllib2
'''
url = 'http://10.10.16.21:50003/ytest/test.php'
response = urllib2.urlopen(url)
print "Response Code: ",response.getcode()

print "Response Header: ",response.headers.getheader('content-type')
print "Response Content: ",response.read()
'''

count = 0
right = 0

while 1:
    url = 'http://10.10.16.21:50003/ytest/test.php'
    response = urllib2.urlopen(url)
    rescode = response.getcode()
    count +=1
    if response.getcode() == 200:
        right +=1
    print  "Count: %d\nSuccess Requests Num.: %d" %(count,right)