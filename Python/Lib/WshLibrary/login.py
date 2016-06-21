import time
from selenium import webdriver

class Login(object):
    def __init__(self):
        pass

    def login(self):
        driver = webdriver.Chrome()
        driver.get('http://betanewwsh.vikduo.com/login/index')
        driver.find_element_by_id('staff_id').send_keys('20151228')
        driver.find_element_by_id('password').send_keys('123456')
        driver.find_element_by_id('captcha').send_keys('1111')
        driver.find_element_by_id('login').click()
        time.sleep(3)
        driver.find_element_by_id('navbar').click()
        driver.find_element_by_xpath("//a[@href='/second-kill/list']").click()

