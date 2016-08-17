# encoding: utf-8
import requests
import json
import Cookie,os
from urllib import urlencode
import settings as set
import re

ws = set.Wsh()

defaultapp = 'android'

class Member(object):
    baseurl = ws.baseurl
    proxylist = {'http' : 'http://127.0.0.1:8888'}
    headers = ws.headers
    headers_json = ws.headers_json


    def __init__(self):
        pass

    def wsh_test(self):
        print "mytest"

    #### 获取活动详情
    def wsh_member_list(self,sessionid):
        # Login
        print u"---Test 获取客户列表---"
        url = self.baseurl+"/member/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        postdata = '{"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"","agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"","createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}'

        r = requests.post(url,data=postdata,headers=headers,cookies=cookies)
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


