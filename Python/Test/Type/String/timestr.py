# encoding: utf-8
import time

a = "2015-09-28 10:00:00"
b = "2016-06-18 12:00:00"
c = "2017-07-19 16:58:58"
now = time.time()

# 转化为时间格式
time.strptime(a,'%Y-%m-%d %H:%M:%S')

# 转化为时间戳
stamps1 = time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
stamps2 = time.mktime(time.strptime(b,'%Y-%m-%d %H:%M:%S'))
stamps_c = time.mktime(time.strptime(c,'%Y-%m-%d %H:%M:%S'))

# 将时间戳转化为localtime
localtime = time.localtime(stamps1)
time.strftime('%Y-%m-%d %H:%M:%S',localtime)

maxt = max(stamps_c,now)
if maxt == now:
    print "Act started."
else:
    print "Act not started yet."

print 'stamps1:',stamps1
print 'stamps2:',stamps2
print 'localtime:',localtime
print max(stamps1,stamps2)
print now



