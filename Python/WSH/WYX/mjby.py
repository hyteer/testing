# encoding: utf-8
import unittest
import time
from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get('http://betanewwsh.vikduo.com/login/index')
driver.find_element_by_id('staff_id').send_keys('20151228')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('captcha').send_keys('1111')
driver.find_element_by_id('login').click()
time.sleep(3)
driver.find_element_by_id('navbar').click()
driver.find_element_by_xpath("//a[@href='/second-kill/list']").click()


#driver.find_element_by_xpath("//div[@id='headactive']//a[@href='/second-kill/list']").click()


