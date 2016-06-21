# encoding: utf-8
from selenium import webdriver
import time

class ComWeb(object):
    def __init__(self):
        pass

    def mytest(self):
        print "mytest"

    def mytest2(self):
        print "mytest2..."

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