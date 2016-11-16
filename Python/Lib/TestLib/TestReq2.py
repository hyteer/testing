#encoding:utf-8
from Lib.YTRequests import ReqLib
import requests,json
from settings import config

cfg = config()
req = ReqLib()
debug=0
headers = {'Content-Type':'application/x-www-form-urlencoded'}


#-----------------获取Session
ss = req.create_session('wsh',url=cfg.URL,debug=1)
print ss.cookies
cookie = req.get_cookie('wsh','PHPSESSID')
cookies = {'PHPSESSID':cookie}

print "cookies:%s" % cookies
data = {'username':cfg.USER,'password':cfg.PASSWORD,'captcha':111}
resp = req.post_request('wsh',url='/login/login-ajax', data=data, headers=headers,debug=debug)

#--------------- 登录微信端
def login_weixin(cookies,debug=0):
    print u"登录微信..."
    ss_wx = req.create_session('wx',url=cfg.URL_WEIXIN,cookies=cookies, debug=debug)
    req.post_request('wx',url='/oauth/testing?id='+cfg.USER_ID, debug=debug)
    return ss_wx

#--------------- 登录分店
def login_subshop(cookies):
    print u"登录分店..."
    ss_sub = req.create_session('sub',url=cfg.URL_TERMINAL,cookies=cookies,debug=debug)
    return ss_sub










