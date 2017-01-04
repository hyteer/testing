import requests
import json
import pytest

class Member(object):
    def member_list(self,conf):
        url = conf.URL+"/member/list-ajax"
        #cookie = fx_api_login(conf)
        postdata = '{"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"",' \
                   '"agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"",' \
                   '"createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}'
        #import pdb
        #pdb.set_trace()
        #print("baseurl:%s" % conf.URL)
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

def member_list2(conf):
        url = conf.URL+"/member/list-ajax"
        #cookie = fx_api_login(conf)
        postdata = '{"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"",' \
                   '"agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"",' \
                   '"createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}'
        #import pdb
        #pdb.set_trace()
        #print("baseurl:%s" % conf.URL)
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode