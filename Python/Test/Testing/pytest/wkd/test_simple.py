import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_username(username):
    assert username == '20161210'

def test_wsh_conf(wsh_conf):
    print "\n",wsh_conf.URL
    print wsh_conf.CAPTCHA
    print wsh_conf.PROXY

def test_get_conf(get_conf):
    print "\n"
    cfg = get_conf("test")
    global cfg
    print "member_id:%s" % cfg.MEMBER_ID
    print "user_id:%s" % cfg.USER_ID

def test_get_conf2():
    #global cfg
    print "user_id:%s" % cfg.USER_ID

def test_wsh_login(wsh_login):
    assert wsh_login() is True
    print("login success...")


def test_float_compare(float_comp):
    x = '0.131'
    y = '0.130'
    print x,y
    assert float_comp(x,y,'no')


