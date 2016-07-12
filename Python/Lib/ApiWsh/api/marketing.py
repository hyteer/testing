# encoding: utf-8
import requests
import json
import Cookie,os
import settings as set

ws = set.Wsh()


class Marketing(object):
    baseurl = ws.baseurl
    proxylist = {'http' : 'http://127.0.0.1:8888'}
    headers = ws.headers

    ######### 销售活动 ##########
    def get_group_actlist(self,sessionid):

        print u"---Test 获取拼团活动列表---"
        url = self.baseurl+"/together-buy/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_reduction_actlist(self,sessionid):

        print u"---Test 获取满减活动列表---"
        url = self.baseurl+"/reduction/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_secondkill_actlist(self,sessionid):

        print u"---Test 获取秒杀活动列表---"
        url = self.baseurl+"/second-kill/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    ######### 推广活动 ##########
    def get_collectzan_actlist(self,sessionid):

        print u"---Test 获取众筹活动列表---"
        url = self.baseurl+"/collect-zan/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r



