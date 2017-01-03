# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_selenium_eg():
    driver = webdriver.Chrome()
    driver.get('http://testnewwsh.snsshop.net/login/index')
    assert driver.title == u"商户后台管理系统1"
    time.sleep(2)
    driver.close()