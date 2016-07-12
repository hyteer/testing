# encoding: utf-8

str = '\xe5\x95\x86\xe5\x9f\x8e'

str2 = str.decode(encoding="utf-8", errors="strict")
str3 = str2+u"测试"
print 'str:',str
print 'str2:',str2
print 'str3:',str3




