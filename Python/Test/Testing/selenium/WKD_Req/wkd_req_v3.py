# coding: utf-8
'''
* 自动刷PV工具
* 使用说明：需安装pyexcel，pyexcel-xlsx三方库
'''
import time
from selenium import webdriver
import sys
import pyexcel as pe
import csv

ENV = '2'
if len(sys.argv) >1:
    ENV = sys.argv[1]
    print "ENV:",ENV

###################################### 获取参数 ####################################

filename = 'wkd_test.csv'
EXCEL_FILE = 'wkd_test.xlsx'
#pages = []
# driver = webdriver.PhantomJS(executable_path='D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
phantom = 'phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
#driver = webdriver.PhantomJS(executable_path=phantom)
counter = 0
WX_URL = "http://nbwshtest.testwkdwx.snsshop.net/NBwshtest"
BACKEND_URL = "http://testwkd.snsshop.net"
SHOP_URL = "http://testwkdshopadmin.snsshop.net"
USERNAME = '20170705'
PASSWORD = '123456'
CAPTCHA = '11'


'''
def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        #yield [unicode(cell, 'utf-8') for cell in row]
        #templist = []
        page = {}
        page['name'] = row[0].decode('utf-8')
        page['url'] = row[1].decode('utf-8')
        pages.append(page)
    print "Pages:",pages
    return pages

reader = unicode_csv_reader(open(filename))

def read_data():
    for page in pages:
        print "Name:%s, Url:%s" % (page['name'],page['url'])

#read_data()
'''

# Read data from excel file
def read_exceldata():
    import pyexcel as pe
    records =  pe.get_array(file_name=EXCEL_FILE)
    for i in range(1,len(records)):
        print("%s, %s") % (records[i][0],records[i][1])

#read_exceldata()
list =  pe.get_array(file_name=EXCEL_FILE)

def get_pages():
    #pages = pe.iget_records(file_name=EXCEL_FILE)
    pages = pe.get_records(file_name=EXCEL_FILE)
    for page in pages:
        print("Name: %s, URL: %s" % (page['name'], page['url']))
    return pages

pages = get_pages()


def base_url(ENV):
    if ENV == '1':
        BASEURL = WX_URL
    elif ENV == '2':
        BASEURL = SHOP_URL
    else:
        BASEURL = BACKEND_URL
    return BASEURL

def init(pages):
    print "Initializing..."
    for page in pages:
        #driver = webdriver.PhantomJS(executable_path=phantom)
        driver = webdriver.PhantomJS()
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
