# encoding: utf-8
import unittest
import time
import json
import sys
import xmlrunner
import HTMLTestRunner

from selenium import webdriver
from args import globalArgs, elements

g = globalArgs
e = elements

# ------------------用户管理-----------------------


class ZfmsOrg(unittest.TestCase):
    desired_caps = g.getEnv()
    ACC = g.randName6X
    NAME = g.randName10X
    PASS = g.randPass6X
    print "Generate randrom user to add, info: \n" + \
        "ID:" + ACC + "\nName:" + NAME + "\nPassword:" + PASS


    @classmethod
    def setUpClass(cls):
        # create a new firefox session
        print u"---用户管理测试初始化...---"

        pf = ZfmsOrg.desired_caps['platform']
        if pf == 'none':
            print "Use local env..."
            cls.driver = webdriver.Firefox()
        else:
            cls.driver = webdriver.Remote('http://172.25.2.71:4444/wd/hub', cls.desired_caps)
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(g.HOME)
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys(g.USERNAME)
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(g.PASSWORD)
        driver.find_element_by_link_text('登录').click()
        url = driver.current_url
        print "URL: ", url
        #cls.assertEqual(g.HOME_LOGINED,url 'URL checking failed')
        driver.find_element_by_id('45').click() # 进入组织管理
        driver.find_element_by_id('leftTree_1_a').click()
        driver.switch_to.frame('46')
        time.sleep(2)

    def test_user_add(self):
        # test user management
        print u"---添加用户---"
        driver = self.driver
        driver.find_element_by_xpath(e.add).click()
        driver.find_element_by_id('account').send_keys(ZfmsOrg.ACC)
        driver.find_element_by_id('password').send_keys(ZfmsOrg.PASS)
        driver.find_element_by_id('fullname').send_keys(ZfmsOrg.NAME)
        time.sleep(1)
        driver.find_element_by_id('dataFormSave').click()
        driver.find_element_by_xpath(e.no).click()
        #driver.find_element_by_xpath(e.back).click()
        time.sleep(2)

    def test_user_bsearch(self):
        # test user management
        print u"---查询用户---"
        driver = self.driver
        driver.find_element_by_xpath("//div[@class='drop']/a[contains(text(),'展开')]").click()
        driver.find_element_by_name('Q_fullname_SL').send_keys(ZfmsOrg.NAME)
        driver.find_element_by_id('btnSearch').click()
        time.sleep(1.5)
        result = driver.find_elements_by_xpath("//table[@id='sysUserItem']/tbody/tr")
        tbNum = len(result)
        if tbNum == 1 and (result[0].get_attribute('class') == 'empty'):
            print u"查询结果为0"
        else:
            print u"查询到 %d 个用户" % tbNum

        time.sleep(1)

    def test_user_del(self):
        # delete user
        driver = self.driver
        print u"---删除用户---"
        result = driver.find_elements_by_xpath("//table[@id='sysUserItem']/tbody/tr")
        tbNum = len(result)
        if tbNum == 1 and (result[0].get_attribute('class') == 'empty'):
            print u"当前页没有找该到用户"
        else:
            time.sleep(1)
            nTb = driver.find_element_by_xpath("//table[@id='sysUserItem']/tbody/tr/td[contains(text(), '"+ZfmsOrg.NAME+"')]")
            nTb.click()
            driver.find_element_by_xpath(e.delete).click()
            time.sleep(1)
            driver.find_element_by_xpath(e.yes).click()
            time.sleep(1)
            driver.find_element_by_xpath(e.confirm).click()


    @classmethod
    def tearDownClass(cls):
        print "Finished and exit."
        time.sleep(4)
        cls.driver.quit()
        pass
