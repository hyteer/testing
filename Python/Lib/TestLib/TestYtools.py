from Lib import Ytools

#ts = Ytools.ApiTest()
cm = Ytools.CommonUtils()
#ts.api_userlogin(debug=1)

### get_path
#path = cm.get_path("D:\\Testing\\Robot","Python")
#print "Path:", path

### Decode
#bystr = '\xe5\x95\x86\xe5\x9f\x8e'
#str = cm.yt_decode(bystr)
#print str

### Get max
'''
x = ''
y = 4
max = cm.yt_get_max(x,y)
print 'max is' ,max

a = 12
b = None
c = cm.yt_sys_max(a,b)
print "max:",c

### Get Max Time
t1 = "2016-07-21 16:58:58"
t2 = "2016-07-21 18:58:58"
maxt = cm.yt_get_maxtime(t1,t2)
print maxt
'''
### yt_act_time_status
t = "2016-07-21 16:58:58"
status = cm.yt_act_time_status(t)
print "status:",status