# coding: utf-8
import requests
import json
import pytest

class Member(object):
    '''
    会员模块相关接口
    '''
    def member_list(self,conf):
        '''
        客户列表
        :param conf:
        :return: content
        '''
        url = conf.URL+"/member/list-ajax"
        postdata = '{"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"",' \
                   '"agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"",' \
                   '"createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}'
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def member_detail(self,conf,user_id):
        '''
        客户详情
        :param conf:
        :param user_id:
        :return: content
        '''
        url = conf.URL+"/member/member-detail-ajax"
        postdata = '{"id":%s}' % user_id
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def members_list(self,conf):
        '''
        会员列表
        :param conf:
        :return: content
        '''
        url = conf.URL+"/members/list-ajax"
        postdata = '{"_page":0,"_page_size":1,"is_get_card":1}'
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def members_detail(self,conf,id):
        '''
        会员详情
        :param conf:
        :param id:
        :return: content
        '''
        url = conf.URL+"/members/detail-ajax"
        postdata = '{"id":%s}' % id
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def member_group_list(self,conf):
        '''
        客户分组列表
        :param conf:
        :return:content
        '''
        url = conf.URL+"/member/group-list-ajax"
        postdata = '{"_page":0,"_page_size":1,"is_get_card":1}'
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content


