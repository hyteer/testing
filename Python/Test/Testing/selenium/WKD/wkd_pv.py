# coding: utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.PhantomJS(executable_path='D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
counter = 0

def wx_login():
    print "--- Weixin Login ---"
    driver.get('http://nbwshtest.testwkdwx.snsshop.net/NBwshtest/oauth/testing?id=13764924')
    driver.implicitly_wait(10)
    time.sleep(1)
    print "Title:%s" % driver.title
    assert driver.title == u"商品列表"


def req_generic(handle,url,name):
    print u"-- 请求" + name + " ----"
    global counter
    driver.switch_to.window(handle)
    driver.get(url)
    time.sleep(2)
    print "Title:%s" % driver.title
    counter += 1

def req_suit1():

    hd_home = driver.current_window_handle
    print driver.current_window_handle
    req_generic(hd_home,'http://nbwshtest.testwkdwx.snsshop.net/NBwshtest/mall/index',u'首页')

    js='window.open("about:blank");'
    driver.execute_script(js)
    hd_product_list = driver.current_window_handle
    print driver.current_window_handle
    req_generic(hd_product_list,'http://nbwshtest.testwkdwx.snsshop.net/NBwshtest/product/category',u'商品列表页')

    handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
    print handles # 输出句柄集合


wx_login()
req_suit1()
time.sleep(3)

'''
while True:
    #driver.get('http://testwkd.snsshop.net/tv-card-coupons/list')
    driver.get('http://testwkd.snsshop.net/hardware/device-response')

    driver.switch_to.window(1)
    print driver.title
    counter += 1
    print "Counter: %d" % counter
    time.sleep(2)
'''

# driver.quit()