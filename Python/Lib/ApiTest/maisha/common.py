# encoding: utf-8
import requests
import json
from urllib import urlencode
import ApiTest.settings as set
ms = set.Maisha()

class MaishaCommon(object):
    baseurl = 'http://huimaidev.vikduo.com/appapi/'
    proxylist = {'http' : 'http://127.0.0.1:8888'}


    def __init__(self):
        pass

    def maisha_test(self):
        print "mytest"

    def _utf8_urlencode(self, data):
        if isinstance(data,unicode):
            return data.encode('utf-8')
        if not isinstance(data,dict):
            return data
        utf8_data={}
        for k, v in data.iteritems():
            utf8_data[k] = unicode(v).encode('utf-8')
            return urlencode(utf8_data)

    def maisha_public_config(self,usersession,app):
        """
        获取用户公共配置信息.

        usersession可通过用户登录接口获取，
        app为测试的平台版本，参数为 android/ios
        """
        print "--test public_config--"
        params = {'usersession': usersession, 'fromapp': app}
        url = self.baseurl + 'common/public_config'
        r = requests.get(url,params=params)
        js = json.loads(r.text)
        error = js['error']

        if r.status_code == 200 and error == 0:
            print "Request sucess, msg:",js['msg']
        else:
            print "Error msg:",js['msg']
            raise Exception("Error,response info:",r.text)
            #
        pass

    def maisha_generate_captcha(self,usersession,app):
        """
        生成图片验证码.

        usersession可通过用户登录接口获取，
        app为测试的平台版本，参数为 android/ios
        """
        print "--test generate_captcha--"
        params = {'usersession': usersession, 'fromapp': app}
        url = self.baseurl + 'common/generate_captcha'
        r = requests.get(url,params=params)
        js = json.loads(r.text)
        error = js['error']

        if r.status_code == 200 and error == 0:
            print "Request sucess, msg:",js['msg']
        else:
            print "Error msg:",js['msg']
            raise Exception("Error,response info:",r.text)
            #
        pass

    def maisha_check_up(self,app):
        """
        查询版本更新.

        app为测试的平台版本，参数为 android/ios
        """
        print "--test check_up--"
        params = {'fromapp': app}
        url = self.baseurl + 'common/check_up'
        r = requests.get(url,params=params)
        js = json.loads(r.text)
        error = js['error']

        if r.status_code == 200 and error == 0:
            print "Request sucess, msg:",js['msg']
        else:
            print "Error msg:",js['msg']
            raise Exception("Error,response info:",r.text)
            #
        pass

    def maisha_get_qrcode(self,usersession,app,content):
        """
        生成二维码.

        usersession可通过用户登录接口获取
        app为测试的平台版本，参数为 android/ios
        """
        print "--test get_qrcode--"
        params = {'usersession': usersession, 'fromapp': app, 'content': content}
        url = self.baseurl + 'common/create_qr'
        r = requests.get(url,params=params)
        ctype = r.headers['Content-Type']
        #print "Content-Type is: ",ctype

        if r.status_code == 200 and ctype == 'image/png':
            print "Request sucess, msg:",r.headers
        else:
            print "Error msg:"
            raise Exception("Error,response info:",r.headers)

    def maisha_getcode(self):
        # todo...
        pass