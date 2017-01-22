# coding: utf-8
import time
from selenium import webdriver
import sys
import csv

ENV = '2'
if len(sys.argv) >1:
    ENV = sys.argv[1]
    print "ENV:",ENV

###################################### 获取参数 ####################################

filename = 'd:\\Res\\csv\\wkd_test.csv'
pages = []


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        #yield [unicode(cell, 'utf-8') for cell in row]
        #templist = []
        page = {}
        page['name'] = row[0].decode('utf-8')
        page['url'] = row[1].decode('utf-8')
        pages.append(page)
        '''
        for item in row:
            item = item.decode('utf-8')
            print "Item:",item
            templist.append(item)
        print "Templist:",templist
        pages.append(templist)
        '''
    print "Pages:",pages
    return pages

reader = unicode_csv_reader(open(filename))

def read_data():
    for page in pages:
        print "Name:%s, Url:%s" % (page['name'],page['url'])

#read_data()



#driver1 = webdriver.Chrome()
# driver = webdriver.PhantomJS(executable_path='D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
phantom = 'D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
#driver1 = webdriver.PhantomJS(executable_path=phantom)
counter = 0
WX_URL = "http://nbwshtest.testwkdwx.snsshop.net/NBwshtest"
BACKEND_URL = "http://testwkd.snsshop.net"
USERNAME = '20170705'
PASSWORD = '123456'
CAPTCHA = '11'

'''
pages = [
    {"name":u"杂志列表","url":"/magazine/list"},
    {"name":u"今日统计","url":"/data-center/today"},
    #{"name":u"杂志列表1","url":"/magazine/list"},
]

pages = [
    {"name":u"杂志列表","url":"/magazine/list"},
    {"name":u"今日统计","url":"/data-center/today"},
    #{"name":u"杂志列表1","url":"/magazine/list"},
]
'''

def base_url(ENV):
    if ENV == '1':
        BASEURL = WX_URL
    else:
        BASEURL = BACKEND_URL
    return BASEURL

def init(pages):
    print "Initializing..."
    for page in pages:
        driver = webdriver.PhantomJS(executable_path=phantom)
        #driver = webdriver.Chrome()
        page['driver'] = driver
    #print pages
    return pages


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

def login_suit(ENV):
    if ENV == '1':   # 前端
        for page in pages:
            wx_login(page['driver'])
            #req_generic(page)
    elif ENV == '2':   # 后台
        for page in pages:
            backend_login(page['driver'])

def run(ENV,pages):
    BASEURL = base_url(ENV)
    init(pages)
    login_suit(ENV)
    while True:
        for page in pages:
            title = req_generic(BASEURL,page)
            if title == u"授权登录":
                wx_login(page[0])

run(ENV,pages)

#run(WX_URL,pages, ENV)
#run(BACKEND_URL,pages,flag=2)

#driver.quit()
