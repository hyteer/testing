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

class Weixin(object):
    capt = cfg.CAPTCHA
    user = cfg.USER
    passwd = cfg.PASSWORD
    baseurl = cfg.URL
    wx_url = cfg.URL_WEIXIN
    terminalurl = cfg.URL_TERMINAL
    proxylist = cfg.PROXY
    headers = cfg.HEADERS
    headers_json = cfg.HEADERS_JSON


    def __init__(self):
        pass

    def wsh_test(self):
        print "mytest"

    #### 获取红包列表(cookie模式)
    def wx_redpack_list_ck(self,sessionid):
        # Login
        print u"---Test 红包列表(cookie模式)---"
        url = self.url = self.wx_url+"/user/redpack-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        data = {'_page':1,'_page_size':10,'is_use':2}

        r = requests.post(url, data=data, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取红包列表(session模式)
    def wx_redpack_list_ss(self,session):
        # Login
        print u"---Test 红包列表(session模式)---"
        url = self.wx_url+"/user/redpack-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        #cookies = {'PHPSESSID': sessionid}
        data = {'_page':1,'_page_size':10,'is_use':2}

        r = session.post(url, data=data, headers=headers)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取商家信息
    def wsh_terminal_list_ajax(self,sessionid):
        # Login
        print u"---分店列表---"
        url = self.terminalurl+"/terminal/list-ajax"
        #url = "http://testshopadmin.snsshop.net/terminal/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r




