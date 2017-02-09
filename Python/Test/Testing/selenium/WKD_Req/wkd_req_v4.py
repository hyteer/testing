# coding: utf-8
'''
* 自动刷PV工具
* 使用说明：需安装pyexcel，pyexcel-xlsx三方库
* 通过PIP安装：pip install pyexcel pyexcel-xlsx
* type:BACK(后台),SHOP(分店)，WX(微信前端)
'''
import time
from datetime import datetime
from selenium import webdriver
import sys
import pyexcel as pe
import csv
import logging

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='WKD_Req.log',
                filemode='w')

if len(sys.argv) >1:
    ENV = sys.argv[1]
    print "ENV:",ENV
else:
    ENV = '1'

###################################### 获取参数 ####################################

filename = 'wkd_test.csv'
EXCEL_FILE = 'wkd_test_v4.xlsx'
#pages = []
# driver = webdriver.PhantomJS(executable_path='D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
PHANTOM = 'phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
#driver = webdriver.PhantomJS(executable_path=phantom)
counter = 0

START_TIME = datetime.now()
USERNAME = '20170705'
PASSWORD = '123456'
CAPTCHA = '11'
REQ_TYPE = '1'
BASE_URLS = {
    'WX': "http://nbwshtest.testwkdwx.snsshop.net/NBwshtest",
    'BACK': "http://testwkd.snsshop.net",
    'SHOP':  "http://testwkdshopadmin.snsshop.net"
}
FLAG = 0    # 用于标题收集标志
RELOGIN_TIMES = 0

########################### Utils ##############################
# Read data from excel file
def read_exceldata():
    import pyexcel as pe
    records =  pe.get_array(file_name=EXCEL_FILE)
    for i in range(1,len(records)):
        print("%s, %s") % (records[i][0],records[i][1])

#read_exceldata()
#list =  pe.get_array(file_name=EXCEL_FILE)


def get_pages():
    global REQ_TYPE
    pages = pe.get_records(file_name=EXCEL_FILE)
    for page in pages:
        print("Type: %s, Name: %s, URL: %s" % (page['type'],page['name'], page['url']))
    return pages

pages = get_pages()


def base_url(ENV):
    if ENV == '1':
        BASEURL = ''
    elif ENV == '2':
        BASEURL = ''
    else:
        BASEURL = ''
    return BASEURL

def init_webdriver(pages):
    print "Initializing..."
    for page in pages:
        #driver = webdriver.PhantomJS(executable_path=PHANTOM)
        driver = webdriver.PhantomJS()
        #driver = webdriver.Chrome()
        page['driver'] = driver
    #print pages
    return pages


def login_wx(driver):
    print "--- Weixin Login ---"
    driver.get('http://nbwshtest.testwkdwx.snsshop.net/NBwshtest/oauth/testing?id=13764924')
    driver.implicitly_wait(10)
    time.sleep(1)
    #print "Title:%s" % driver.title
    assert driver.title == u"商品列表"
    print u"登录成功"

def login_backend(driver):
    print u"--- 后台登录 ---"
    driver.get('http://testwkd.snsshop.net')
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_id('staff_id').send_keys(USERNAME)
    time.sleep(0.5)
    driver.find_element_by_id('password').send_keys(PASSWORD)
    time.sleep(0.5)
    driver.find_element_by_id('captcha').send_keys(CAPTCHA)
    time.sleep(0.5)
    driver.find_element_by_id('login').click()
    driver.maximize_window()
    print "Title:%s" % driver.title

    #assert driver.title == u"概况"
    print u"登录成功"

def login_shop(driver):
    print u"--- 分店登录 ---"
    driver.get('http://testwkd.snsshop.net')
    driver.implicitly_wait(10)
    driver.find_element_by_id('staff_id').send_keys(USERNAME)
    time.sleep(0.5)
    driver.find_element_by_id('password').send_keys(PASSWORD)
    time.sleep(0.5)
    driver.find_element_by_id('captcha').send_keys(CAPTCHA)
    time.sleep(0.5)
    driver.find_element_by_id('login').click()
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_link_text(u'微分店').click()
    #print "Title:%s" % driver.title

    #assert driver.title == u"概况"
    print u"登录成功"


def req_generic(page):
    #import pdb
    #pdb.set_trace()
    global RELOGIN_TIMES
    global counter
    BASEURL = BASE_URLS[page['type']]

    driver = page['driver']
    url = BASEURL + page['url']
    print "URL:%s" % url
    driver.get(url)
    counter += 1
    # Test session timeout
    if counter == 5 or 10:
        driver.delete_all_cookies()

    log = u"-- %s,%s,总数:%d [开始时间:%s]----" %(page['type'],driver.title,counter,START_TIME)
    print log
    logging.info(log)
    #logging.info('This is info message')
    #logging.warning('This is warning message')
    #time.sleep(2)
    if page.has_key('title'):
        if page['title'] != driver.title:
            print "Session 已过期，准备重新登录"

            login_generic(page)
            RELOGIN_TIMES += 1
            print "ReloginTimes:",RELOGIN_TIMES
            logging.warning('Session过期重登录次数：%d' %RELOGIN_TIMES)
    else:
        page['title'] = driver.title

    return driver.title

def login_generic(page):
    if page['type'] == 'WX':   # 前端
        login_wx(page['driver'])
    if page['type'] == 'SHOP':  # 分店
        login_shop(page['driver'])
    else:   # 后台
        login_backend(page['driver'])

def login_suit(pages):
    for page in pages:
        login_generic(page)



def run(pages):
    init_webdriver(pages)
    login_suit(pages)
    while True:
        for page in pages:
            title = req_generic(page)
            if title == u"授权登录":
                login_wx(page[0])

run(pages)

#run(WX_URL,pages, ENV)
#run(BACKEND_URL,pages,flag=2)
#driver.quit()
