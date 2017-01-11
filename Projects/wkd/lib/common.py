# coding: utf-8
'''
通用模块配置
'''
import Cookie
import json

import chardet,time
import requests
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from param.utils import Utils

utils = Utils()
import sys
print "default coding:",sys.getdefaultencoding()
print "stdin:", sys.stdin.encoding
print "stdout:", sys.stdout.encoding


class Common(object):

    def login(self,conf,driver):
        '''
        微客多管理后台登录
        :param conf:
        :param driver:
        :return:True
        '''
        #driver = webdriver.Chrome()
        driver.get(conf.URL)

        Config.driver = driver    # 注册driver
        driver.implicitly_wait(10)
        assert driver.title == conf.TITLE
        driver.find_element_by_id('staff_id').send_keys(conf.USERNAME)
        time.sleep(0.5)
        driver.find_element_by_id('password').send_keys(conf.PASSWORD)
        time.sleep(0.8)
        driver.find_element_by_id('captcha').send_keys('11')
        time.sleep(0.5)
        driver.find_element_by_id('login').click()
        driver.maximize_window()
        #import pdb
        #pdb.set_trace()
        banner = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("navbar"))

        assert driver.title == u"概况"
        brand_text = driver.find_element_by_xpath("//div[@id='top-left']/a[@class='navbar-brand']/small").text

        if conf.DEBUG == 'yes':
            print banner.tag_name
            print utils.utf8_filter(banner.text)
            print banner.get_attribute("class")
            print "Title:%s" % utils.utf8_filter(driver.title)
            print utils.utf8_filter(brand_text)

        return True

    def wx_login(self,conf,driver):
        '''
        微信前端页登录
        :param conf:
        :param driver:
        :return:True
        '''
        #driver = webdriver.Chrome()
        URL = conf.WX_URL + "/oauth/testing?id=" + conf.USER_ID
        driver.get(URL)
        conf.wx_driver = driver

        return True

    def api_login(self,conf):
        '''
        登录微商户API
        Returns:sessionid
        '''
        baseurl = conf.URL
        headers = conf.HEADERS
        captcha = conf.CAPTCHA
        username = conf.USERNAME
        password = conf.PASSWORD
        ssid = conf.SSID

        r = requests.get(baseurl, headers=headers)
        #cookies = r.headers['Set-Cookie']
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







