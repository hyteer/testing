# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_env(conf):
    print "TestEnv:%s" % conf.ENV
    assert 1

def test_config(conf):
    print "member_id:%s" % conf.MEMBER_ID
    print "user_id:%s" % conf.USER_ID

def test_username(username):
    assert username == '20161210'

def test_get_conf(conf):
    print "user_id:%s" % conf.USER_ID


def test_wsh_login(conf,wsh_login,u8filter):
    assert wsh_login(conf,u8filter) is True
    print("login success...")


def test_float_compare(float_comp):
    x = '0.131'
    y = '0.130'
    print x,y
    assert float_comp(x,y,'no')

def test_debug_flag(conf):
    print conf.DEBUG

def test_api_login(conf,fx_api_login):
    ssid = fx_api_login(conf)
    print "SSID:", ssid
    conf.ssid = ssid
    print conf.ssid



