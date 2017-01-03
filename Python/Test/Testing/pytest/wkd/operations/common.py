# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
import Cookie
from ..config import get_config,Config





def login():
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
    print banner.tag_name
    print banner.text
    print banner.get_attribute("class")

    #print "Banner:%r" % str(banner.text())

    print u"Title:%s" % driver.title
    assert driver.title == u"概况"
    print driver.find_element_by_xpath("//div[@id='top-left']/a[@class='navbar-brand']/small").text
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
    cookies = r.headers['Set-Cookie']
    #cookie = re.match("'PHPSESSID':'(.+?)',.", cookies)
    #cookies.load(headers['Set-Cookie'])
    #print cookies
    #session = cookies['PHPSESSID'].value
    cookie = Cookie.SimpleCookie(r.headers['Set-Cookie'])
    sessionid = cookie['PHPSESSID'].value

    #js = json.loads(cookies)
    print "Headers:",r.headers
    #print "Cookies:",r.cookies
    #print "Raw:",r.raw
    #print "Set-Cookie:",r.headers['Set-Cookie']
    print "cookies:", cookies
    print "SessionID:", sessionid
    Config.SSID = sessionid
    print "Config::SSID:%s" % conf.SSID

    # Login
    print "--- API Login ---"
    url = baseurl+"/login/login-ajax"
    #url = 'http://betanewwsh.vikduo.com/login/login-ajax'
    headers = headers
    postdata = {'captcha': captcha, 'username': username, 'password': password}
    cookies = {'PHPSESSID': sessionid}

    r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
    #length = len(r.text)
    #js = json.loads(r.text[1:length])

    print "headers:",r.headers
    print u"Response:%s" % (r.content).decode('utf-8')
    #print "Response:", r.text[1:length]
    print "length:", len(r.text)

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



