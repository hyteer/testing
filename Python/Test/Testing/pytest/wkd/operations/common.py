# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
import Cookie
from ..config import get_config,Config
import tools
import chardet





def login(conf,u8filter):
    driver = webdriver.Chrome()
    driver.get('http://testnewwsh.snsshop.net/login/index')
    driver.implicitly_wait(10)
    assert driver.title == u"商户后台管理系统"
    driver.maximize_window()
    driver.find_element_by_id('staff_id').send_keys('20161210')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('captcha').send_keys('11')
    driver.find_element_by_id('login').click()
    #import pdb
    #pdb.set_trace()
    banner = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("navbar"))

    assert driver.title == u"概况"
    brand_text = driver.find_element_by_xpath("//div[@id='top-left']/a[@class='navbar-brand']/small").text

    if conf.DEBUG == 'yes':
        print banner.tag_name
        print tools.utf8_filter(banner.text)
        print banner.get_attribute("class")
        print "Title:%s" % tools.utf8_filter(driver.title)
        print tools.utf8_filter(brand_text)

    return True

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

    if conf.DEBUG == 'yes':
        #print "Cookies:",r.cookies
        #print "Raw:",r.raw
        print "cookies:", cookies
        print "SessionID:", sessionid
        Config.SSID = sessionid
        print "Config::SSID:%s" % conf.SSID
        print "Headers:",r.headers
        print "headers:",r.headers
        #length = len(r.text)
        #print "Response:", r.text[1:length]
        print "r.content char:",chardet.detect(r.content)
        print "r.text:", tools.utf8_filter(r.text)

    return cookies



def float_compare(x,y,flag="yes"):
    print "x:%s,y:%s" % (x,y)
    if flag == "yes":
        assert float(x) == float(y)
        return True
    else:
        assert float(x) != float(y)
        return True

def floa_not_equalst(x,y):
    print "x:%s,y:%s" % (x,y)
    assert float(x) != float(y)
    return True



