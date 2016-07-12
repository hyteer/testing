from Lib import Ytools

#ts = Ytools.ApiTest()
cm = Ytools.CommonUtils()
#ts.api_userlogin(debug=1)

# get_path
#path = cm.get_path("D:\\Testing\\Robot","Python")
#print "Path:", path

# Decode
bystr = '\xe5\x95\x86\xe5\x9f\x8e'
str = cm.yt_decode(bystr)
print str