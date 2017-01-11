# coding: utf-8
'''
初始化模块配置
'''
import Cookie
import json

import chardet
import requests

from config import Config
from param.utils import Utils

utils = Utils()

def api_login(conf):
    '''
    登录微商户API
    Returns:sessionid
    '''
    baseurl = conf.URL
    headers = conf.HEADERS
    captcha = conf.CAPTCHA
    username = conf.USERNAME
    password = conf.PASSWORD

    r = requests.get(baseurl, headers=headers)
    cookie = Cookie.SimpleCookie(r.headers['Set-Cookie'])
    sessionid = cookie['PHPSESSID'].value
    # Login
    print "--- API Login ---"
    url = baseurl+"/login/login-ajax"
    postdata = {'captcha': captcha, 'username': username, 'password': password}
    cookies = {'PHPSESSID': sessionid}

    r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
    data = json.loads(r.text)
    errcode = data['errcode']
    print "errcode:", data['errcode']
    assert errcode == '0'
    Config.SSID = sessionid
    Config.COOKIE = {'PHPSESSID': sessionid}

    if conf.DEBUG == 'yes':
        str = u"-------------【调试】------------"
        print utils.utf8_filter(str)
        #print "Cookies:",r.cookies
        #print "Raw:",r.raw
        print "cookies:", cookies
        print "SessionID:", sessionid
        print "Config::SSID:%s" % conf.SSID
        print "Headers:",r.headers
        print "headers:",r.headers
        #length = len(r.text)
        #print "Response:", r.text[1:length]
        print "r.content char:",chardet.detect(r.content)
        print "r.text:", utils.utf8_filter(r.text)

    return cookies




