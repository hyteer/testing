"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        #app = os.path.abspath('../../apps/TestApp/build/release-iphonesimulator/TestApp.app')
        #app = os.path.abspath('D:\\apps\TestApp\\build\\release-iphonesimulator\\TestApp.app')
        self.driver = webdriver.Remote(
            command_executor='http://10.20.100.82:4731/wd/hub',
            desired_capabilities={
               # 'app': app,
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 6s',
                'udid':'2bc289b87f8fdadd6add2ad0b55a26c6081d2d77'
            })

    def tearDown(self):
        self.driver.quit()

    def test_category(self):
        # populate text fields with two random numbers
        cls = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]')
        cls.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
