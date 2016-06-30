# encoding: utf-8
#from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from appium import webdriver
from SongzAppiumLibrary.utils import ApplicationCache
from SongzAppiumLibrary.locators import ElementFinder
from SongzAppiumLibrary.keywords.keywordgroup import KeywordGroup
import ast
# added by songz
from robot.utils import timestr_to_secs
# added by songz
import time

class Common(object):
    def __init__(self):
        pass

    def getSlideArgsV(self,device):
        if device == 'small':   # 400x800
            hx1 = 240;hy1 = 580
            hx2 = 240;hy2 = 240
        if device == 'medium':
            hx1 = 350;hy1 = 950
            hx2 = 350;hy2 = 400
        if device == 'big':
            hx1 = 500;hy1 = 1400
            hx2 = 500;hy2 = 400
        return hx1,hy1,hx2,hy2

        print "hx1:%s,hx2:%s\nhx2:%s,hy2:%s"%(hx1,hy1,hx2,hy2)

    def getSlideArgsH(self,device):
        if device == 'small':   # 400x800
            hx1 = 350;hy1 = 500
            hx2 = 150;hy2 = 500
        if device == 'medium':   # Medium
            hx1 = 600;hy1 = 800
            hx2 = 180;hy2 = 800
        if device == 'big':   # Big
            hx1 = 900;hy1 = 1000
            hx2 = 300;hy2 = 1000

    def demo(self):
        print "This is a demo for AppiumYT..."

    def demo_title_should_be(self,expected):
        # a demo by YT for implemnting the same function as 'Title Should Be'
        seleniumlib = BuiltIn().get_library_instance('Selenium2Library')
        title = seleniumlib.get_title()
        if not title.startswith(expected):
            raise AssertionError("Title '%s' did not start with '%s'"
                                 % (title, expected))

    def demo_get_size(self,locator):
        # not implement yet
        driver = self._current_application()


        appiumlib = BuiltIn().get_library_instance('SongzAppiumLibrary')

        appiumlib.get_window_size()['width']
        appiumlib.get_window_size()['height']
        pass

    def demo_input_text(self,locator,text):
        # a demo by YT for implemnting the same function as 'Input Text'
        """Description:
        Types the given `text` into text field identified by `locator`.
        See `introduction` for details about locating elements.
        """
        appiumlib = BuiltIn().get_library_instance('SongzAppiumLibrary')
        appiumlib._info("Typing text '%s' into text field '%s'" % (text, locator))
        appiumlib._element_input_text_by_locator(locator, text)

# *********************Others***************************
    def login(self,user,password,captcha):

        driver = webdriver.Chrome()
        driver.get('http://betanewwsh.vikduo.com/login/index')
        driver.find_element_by_id('staff_id').send_keys(user)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('captcha').send_keys(captcha)
        driver.find_element_by_id('login').click()
        time.sleep(3)
        driver.find_element_by_id('navbar').click()
        driver.find_element_by_xpath("//a[@href='/second-kill/list']").click()