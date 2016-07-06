# encoding: utf-8
import requests
import json
from urllib import urlencode
from ApiTest import settings as set


class MaishaCommon(object):
    baseurl = 'http://huimaidev.vikduo.com/appapi/'
    proxylist = {'http' : 'http://127.0.0.1:8888'}
    ms = set.Maisha()

    def __init__(self):
        pass


####################### Common ##########################

    def maisha_public_config(self,usersession,app='android'):
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

    def maisha_send_vercode(self,usersession,app='android',action='reg'):
        """
        发送验证码.

        用于手机注册，找回密码，绑定手机等的验证码发送<br>
        test\n
        usersession可通过用户登录接口获取，
        app为测试的平台版本，参数为 android/ios
        """
        print "--test loading_ad--"
        params = {'usersession': usersession, 'fromapp': app, 'action': action}
        url = self.baseurl + 'common/generate_captcha'
        r = requests.get(url,params=params)
        js = json.loads(r.text)
        error = js['error']

        if r.status_code == 200 and error == 0:
            print "Request sucess, msg:",js['msg']
        else:
            print "Error msg:",js['msg']
            raise Exception("Error,response info:",r.text)

    def maisha_generate_captcha(self,usersession,app='android'):
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

    def maisha_loading_ad(self,usersession,app='android'):
        """
        获取首页加载广告.

        usersession可通过用户登录接口获取，
        app为测试的平台版本，参数为 android/ios
        """
        print "--test loading_ad--"
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

    def maisha_check_up(self,app='android'):
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

    def maisha_get_qrcode(self,usersession,content,app='android'):
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

    def maisha_upload_file(self):
        # todo...
        pass

    def maisha_getcode(self):
        # todo...
        pass