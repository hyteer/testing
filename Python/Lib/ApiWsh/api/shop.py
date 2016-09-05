# encoding: utf-8
import requests
import json
import Cookie,os
from urllib import urlencode
import re
from settings import config

cfg = config()
#ws = set.Wsh()

defaultapp = 'android'

class Shop(object):
    capt = cfg.CAPTCHA
    user = cfg.USER
    passwd = cfg.PASSWORD
    baseurl = cfg.URL
    proxylist = cfg.PROXY
    headers = cfg.HEADERS
    headers_json = cfg.HEADERS_JSON


    def __init__(self):
        pass

    def wsh_test(self):
        print "mytest"

    #### 获取活动详情
    def wsh_actlist(self,sessionid):
        # Login
        print u"---Test 活动详情---"
        url = self.baseurl+"/reduction/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取商家信息
    def wsh_shop_get(self,sessionid):
        # Login
        print u"---Test 获取商家信息---"
        url = self.baseurl+"/shop/get-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r


