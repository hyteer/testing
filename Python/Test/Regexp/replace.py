import re
from Regexp import searchByDelimiter


content ="'10.10.16.41', '10.10.16.42', '10.10.16.43', '10.10.16.44', '10.10.16.45', '10.10.16.46', '10.10.16.47', '10.10.16.48', '10.10.16.49', '10.10.16.50', '10.10.16.51', '10.10.16.52', '10.10.16.53', '10.10.16.54', '10.10.16.55', '10.10.16.56', '10.10.16.57', '10.10.16.58'"
str = content.replace("'",'').replace(" ","")
print "str: ",str
hosts = searchByDelimiter.tsplit(str,(','))


print "Hosts:%d\n%s"%(len(hosts),hosts)
print "The third host is: ",hosts[2]


