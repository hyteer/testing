# coding: utf-8
"""
基本功能测试
"""
import time
from selenium import webdriver
import pytest



class TestBasic:

    wx = None

    @pytest.fixture
    def setup(self,conf,load_mod):
        assert load_mod('weixin') is True
        wx = conf.LOADED_MODULES['weixin']
        self.wx = wx
        self.conf = conf
        return conf

    # 登录
    def test_wsh_login(self,conf):
        driver = webdriver.Chrome()
        cm = conf.COMMON
        cm.login(conf,driver)
        time.sleep(1)
        print("login success...")
        driver.find_element_by_link_text('微店铺').click()
        time.sleep(2)
        driver.close()

    def test_wx_login(self,conf):
        driver = webdriver.Chrome()
        cm = conf.COMMON
        cm.wx_login(conf,driver)
        time.sleep(2)
        xpath =  conf.WX_MENU.BOTTOM['cart']
        driver.find_element_by_xpath(xpath=xpath).click()
        time.sleep(2)
        driver.close()











