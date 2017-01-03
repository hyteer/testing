# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait




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



