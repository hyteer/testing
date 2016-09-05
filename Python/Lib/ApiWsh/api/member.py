# encoding: utf-8
import requests
import json
import Cookie,os
from urllib import urlencode
#import settings as set
import re
from settings import config

cfg = config()

#ws = set.Wsh()

defaultapp = 'android'

class Member(object):
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

    #### 获取客户列表
    def wsh_member_list(self,sessionid):
        # Login
        print u"---Test 获取客户列表---"
        url = self.baseurl+"/member/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        postdata = '{"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"",' \
                   '"agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"",' \
                   '"createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}'

        r = requests.post(url,data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取客户详情
    def wsh_member_detail_ajax(self,sessionid):
        # Login
        print u"---Test 获取客户详情---"
        url = self.baseurl+"/member/member-detail-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        postdata = '{"id": 13764502}'

        r = requests.post(url,data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取客户积分列表
    def wsh_member_point_list(self,sessionid):
        # Login
        print u"---Test 获取客户积分列表---"
        url = self.baseurl+"/member/point-list-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        postdata = '{"_page":1,"_page_size":20,"type_id":1,"id":"11540725"}'

        r = requests.post(url,data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取会员列表
    def wsh_members_list_ajax(self,sessionid):
        # Login
        print u"---Test 获取会员列表---"
        url = self.baseurl+"/members/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        postdata = '{"_page":1,"_page_size":20,"keyword":"","real_name":"",' \
                   '"create_start":"","create_end":"","bind_mobile":"","status":[],' \
                   '"source":[],"level":[],"member_group_id":[],"tags":[],"sex":[],' \
                   '"city_id":[],"city":[],"shop_sub_id":""}'

        r = requests.post(url,data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取会员详情
    def wsh_members_detail(self,sessionid,id=259):
        # Login
        print u"---Test 获取会员详情---"
        url = self.baseurl+"/members/detail-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        postdata = '{"id":%d}' % id

        r = requests.post(url,data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取会员标签
    def wsh_members_get_tag(self,sessionid):
        # Remark
        print u"---Test 获取会员标签---"
        url = self.baseurl+"/members/get-tag-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        postdata = '{"id":259}'

        r = requests.post(url,data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r

    #### 获取会员全部分组
    def wsh_members_get_all_tags(self,sessionid):
        # Remark
        print u"---Test 获取会员全部分组---"
        url = self.baseurl+"/members/find-all-group-ajax"

        headers = self.headers_json
        cookies = {'PHPSESSID': sessionid}
        #postdata = '{"id":259}'

        r = requests.post(url,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content

        return r



