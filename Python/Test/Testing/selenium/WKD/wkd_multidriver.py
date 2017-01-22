# coding: utf-8
import time
from selenium import webdriver

'''
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
#driver3 = webdriver.Chrome()
#driver4 = webdriver.Chrome()
#driver5 = webdriver.Chrome()
'''
#
# driver = webdriver.PhantomJS(executable_path='D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
phantom = 'D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'

#driver1 = webdriver.PhantomJS(executable_path=phantom)
#driver2 = webdriver.PhantomJS(executable_path=phantom)
#driver3 = webdriver.PhantomJS(executable_path=phantom)
#driver4 = webdriver.PhantomJS(executable_path=phantom)
#driver5 = webdriver.PhantomJS(executable_path=phantom)
#driver6 = webdriver.PhantomJS(executable_path=phantom)

counter = 0
WX_URL = "http://nbwshtest.testwkdwx.snsshop.net/NBwshtest"
BACKEND_URL = "http://testwkd.snsshop.net"
USERNAME = '20170705'
PASSWORD = '123456'
CAPTCHA = '11'
'''
pages = [
    #[driver1,u"首页","/NBwshtest/mall/index"],
    #[driver2,u"商品列表页","/NBwshtest/product/category"],
    #[driver2,u"商品列表页","/NBwshtest/product/category"],
    #[driver1,u"个人中心","/NBwshtest/user/home"],
    #[driver2,u"惊喜页","/NBwshtest/surprise/index"],
    #[driver3,u"购物车页面","/NBwshtest/cart/index"],
    #[driver4,u"秒杀活动","/NBwshtest/second-kill/list"],
    [driver1,u"拼团活动","/together-buy/detail?id=513&act_id=2808"],
    [driver2,u"众筹活动","/collect-zan/zan?id=854"],
    #[driver4,u"大转盘","/NBwshtest/cart/index"],
    #[driver3,u"砸金蛋","/market-activity/activity?id=2782"],
    #[driver4,u"商城红包","/grouppack/receive?id=2777"],
    #[driver5,u"预约活动","/reserve/detail?id=656"],
    #[driver6,u"记忆翻翻看","/memory-fan/activity?id=62"],
    #[driver5,u"活动过期跳转页","/NBwshtest/user/home"],
    ###################################################
    [driver5,u"杂志列表","/magazine/list"],
]
'''

pages = [
    {"name":u"杂志列表","url":"/magazine/list"},
    {"name":u"今日统计","url":"/data-center/today"},
    #{"name":u"杂志列表1","url":"/magazine/list"},
]
def gen_pages(pages):
    for page in pages:
        driver = webdriver.PhantomJS(executable_path=phantom)
        #driver = webdriver.Chrome()
        page['driver'] = driver
    print pages
    return pages

gen_pages(pages)


def wx_login(driver):
    print "--- Weixin Login ---"
    driver.get('http://nbwshtest.testwkdwx.snsshop.net/NBwshtest/oauth/testing?id=13764924')
    driver.implicitly_wait(10)
    time.sleep(1)
    #print "Title:%s" % driver.title
    assert driver.title == u"商品列表"
    print u"登录成功"

def backend_login(driver):
    print u"--- 后台登录 ---"
    driver.get('http://testwkd.snsshop.net')
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element_by_id('staff_id').send_keys(USERNAME)
    time.sleep(0.5)
    driver.find_element_by_id('password').send_keys(PASSWORD)
    time.sleep(0.8)
    driver.find_element_by_id('captcha').send_keys(CAPTCHA)
    time.sleep(0.5)
    driver.find_element_by_id('login').click()
    driver.maximize_window()
    print "Title:%s" % driver.title

    #assert driver.title == u"概况"
    print u"登录成功"


def req_generic(BASEURL,page):
    #import pdb
    #pdb.set_trace()
    print u"-- 请求" + page['name'] + " ----"
    global counter
    driver = page['driver']
    url = BASEURL + page['url']
    print "URL:%s" % url
    driver.get(url)
    counter += 1
    print "Title:%s, Counter:%d" % (driver.title,counter)
    return driver.title

def login_suit(flag):
    if flag == 1:   # 前端
        for page in pages:
            wx_login(page['driver'])
            #req_generic(page)
    if flag == 2:   # 后台
        for page in pages:
            backend_login(page['driver'])

def run(BASEURL,pages,flag=2):
    login_suit(flag)
    while True:
        for page in pages:
            title = req_generic(BASEURL,page)
            if title == u"授权登录":
                wx_login(page[0])

#run(WX_URL,pages)
run(BACKEND_URL,pages,flag=2)


# driver.quit()

