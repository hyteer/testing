# encoding: utf-8
import requests
import json
from urllib import urlencode
from ApiTest import settings as set
ms = set.Maisha()

class MaishaUser(object):
    baseurl = 'http://huimaidev.vikduo.com/appapi/'
    proxylist = {'http' : 'http://127.0.0.1:8888'}



    def __init__(self):
        pass

    def maisha_test(self):
        print "mytest"

######################## User ###########################
    def maisha_user_login(self,phone,password,app='android',debug=0):
    #def maisha_user_login(self,app,phone=ms,debug=0,**args):
        """
        用户登录

        app为测试的平台版本，参数为 android/ios

        登录返回值为usersession
        """
        print "--test user_login--"
        url = ms.baseurl + 'user/login'
        usersession = 'nothing'

        if debug == 1:
            print "Debug info:"

        postdata = {'fromapp': app, 'phone': phone, 'password': password}
        r = requests.post(url, data=postdata)
        #r = requests.post(url, data=postdata, proxies=self.proxylist)  # Use proxy
        #print "Response:",r.content
        #print "msg:",js['msg']
        #print "type:",js['type']
        js = json.loads(r.text)
        error = js['error']

        if r.status_code == 200 and error == 0:
            usersession = js['data']['usersession']
            print "Request sucess, msg:",js['msg']
            print "username:",js['data']['username']
            print "usersession:",usersession
        else:
            print "Error msg:",js['msg']
            raise Exception("Error,response info:",r.text)

        return usersession

    def maisha_user_getinfo(self,usersession,app='android'):
        """
        获取用户信息.

        usersession可通过用户登录接口获取
        app为测试的平台版本，参数为 android/ios
        """
        print "--test user_getinfo--"
        params = {'usersession': usersession, 'fromapp': app}
        url = self.baseurl + 'user/get_info'
        r = requests.get(url,params=params)
        js = json.loads(r.text)
        error = js['error']

        if r.status_code == 200 and error == 0:
            print "Request sucess, msg:",js['type']
        else:
            print "Error msg:",js['msg']
            raise Exception("Error,response info:",r.text)
            #
        pass

    def maisha_user_get_store_info(self,usersession,app='android'):
        """
        获取店铺信息.

        获取分销商店铺信息

        usersession可通过用户登录接口获取
        app为测试的平台版本，参数为 android/ios
        """
        print "--test user_getinfo--"
        params = {'usersession': usersession, 'fromapp': app}
        url = self.baseurl + 'user/get_info'
        r = requests.get(url,params=params)
        js = json.loads(r.text)
        error = js['error']

        if r.status_code == 200 and error == 0:
            print "Request sucess, msg:",js['type']
        else:
            print "Error msg:",js['msg']
            raise Exception("Error,response info:",r.text)
