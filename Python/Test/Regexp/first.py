# -*- coding: UTF-8 -*-

import re
str = "This is a simple test program for demonstrating the use of regexp."

rg1 = re.match('is',str)
rg2 = re.search('is',str).span()
rg3 = re.findall('fore',str)
rg4 = re.findall('e',str)

print rg2
if rg3:
    print "rg3: ",rg3
else:
    print "rg3 is None..."

print "rg4: %s, Length: %d"%(rg4,len(rg4))

print(re.match('This',str).span())  # 在起始位置匹配
print(re.match('for', str))         # 不在起始位置匹配
print str[0:3]

