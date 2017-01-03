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
#g.setBrowser('chrome')
#g.setPlatform('WINDOWS')

# ------------------用户管理-----------------------
'''
def getGlb(pf,br):
    g.setPlatform(pf)
    g.setBrowser(br)
    BROWSER = g.getBrowser()
    print "Get Browser: " + BROWSER

    PLATFORM = g.getPlatform()
    desired_caps = {
            'platform': PLATFORM,
            'browserName': BROWSER
            # 'platform': "WINDOWS",
            #'browserName': "firefox"

        }
    print "Get desired_caps: " + str(desired_caps)
'''
class ZfmsOrg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        desired_caps = g.getGlb()
        print "Get glb: " + str(desired_caps)
        # create a new firefox session
        print "---用户管理测试初始化...---"
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.implicitly_wait(30)

    def test_Temp(self):
        self.driver.get(g.HOME)

    @classmethod
    def tearDownClass(cls):
        print "Finished and exit."
        time.sleep(2)
        cls.driver.quit()
        pass