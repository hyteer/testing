# encoding: utf-8
import requests
import json
import Cookie,os
from urllib import urlencode
from utils import CommonUtils
import settings as set
ws = set.Wsh()


class Common(object):
    baseurl = ws.baseurl
    proxylist = {'http' : 'http://127.0.0.1:8888'}
    headers = ws.headers
    capt = ws.captcha
    user = ws.user
    passwd = ws.password



    def __init__(self):
        pass

    #### 获取Cookie
    def wsh_get_cookie(self):

        print "---Test get cookie---"
        url = self.baseurl+'/captcha/getimage'
        #url = 'http://betanewwsh.vikduo.com/reduction/list-ajax'
        headers = self.headers

        r = requests.get(url, headers=headers)
        cookies = r.headers['Set-Cookie']
        #cookie = re.match("'PHPSESSID':'(.+?)',.", cookies)
        #cookies.load(headers['Set-Cookie'])
        #print cookies
        #session = cookies['PHPSESSID'].value
        cookie = Cookie.SimpleCookie(r.headers['Set-Cookie'])
        sessionid = cookie['PHPSESSID'].value

        #js = json.loads(cookies)

        print "Headers:",r.headers
        #print "Cookies:",r.cookies
        #print "Raw:",r.raw
        #print "Set-Cookie:",r.headers['Set-Cookie']
        print "cookies:", cookies
        print "SessionID:", sessionid
        return sessionid

    #### 登录获取SessionID
    def wsh_login(self,sessionid):
        # Login
        print "--- Test Login ---"
        url = self.baseurl+"/login/login-ajax"
        #url = 'http://betanewwsh.vikduo.com/login/login-ajax'
        headers = self.headers
        postdata = {'captcha': self.capt, 'username': self.user, 'password': self.passwd}
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
        #length = len(r.text)
        #js = json.loads(r.text[1:length])

        print "headers:",r.headers
        print "Response:", r.content
        #print "Response:", r.text[1:length]
        print "length:", len(r.text)
        #print "errcode:",js['errcode'],"errmsg:",js['errmsg']

        return r.text





