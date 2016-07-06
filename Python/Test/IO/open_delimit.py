import re
from Regexp import searchByDelimiter

file = open("d:/temp/hosts.txt","r")
content = file.read()
str = content.replace(',','')
list = searchByDelimiter.tsplit(str,('\n'))

#hosts = list.replace(',','')


print "Hosts:\n",list

print file
print "File name: %s"%(file.name)
print "File content: %s"%(file.read())
