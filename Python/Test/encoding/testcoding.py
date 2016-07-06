# encoding: utf-8

str = u'登录测试'
str2 = u'\u8bf7\u5148\u767b\u5f55'
ustr = str.encode("utf-8")

print str2
print ustr
raise Exception("Error:",ustr,str2)
