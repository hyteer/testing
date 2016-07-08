# encoding: utf-8
import requests
import json
import Cookie,os
from urllib import urlencode
import settings as set
import re

ws = set.Wsh()

defaultapp = 'android'

class Shop(object):
    baseurl = ws.baseurl
    proxylist = {'http' : 'http://127.0.0.1:8888'}
    headers = ws.headers


    def __init__(self):
        pass

    def wsh_test(self):
        print "mytest"


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

    def wsh_shop_get(self,sessionid):
        # Login
        print u"---Test 获取商家信息接口---"
        url = self.baseurl+"/shop/get-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r


