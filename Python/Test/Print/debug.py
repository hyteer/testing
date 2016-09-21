# encoding:utf-8
import time
from datetime import datetime

str = u"测试组"
ustr = str.encode('utf-8')
print "ustr:",ustr

print "-------- Time --------"
stamp = 1472024262
local_dt = datetime.fromtimestamp(stamp)
print "time:",local_dt

########## Wechat ##########
print u'\u5546\u57ce'
print u'\u4e0d\u5141\u8bb8'
str11 = '\xb7\xc7\xd1\xa1\xd4\xf1\xd0\xd4\xb5\xc4\xb2\xce\xca\xfd\xa1\xa3'
str111 = str11.decode("GBK")
print "str111:",str111
print u'\u60a8\u63d0\u4ea4\u7684\u6570\u636e\u6709\u8bef'