# encoding: utf-8
import unittest
import time
from selenium import webdriver



driver = webdriver.Chrome()

#driver = webdriver.Firefox()
driver.get('http://betanewwsh.snsshop.net/login/index')

driver.maximize_window()
#driver.implicitly_wait(5)
driver.find_element_by_id('staff_id').send_keys('20151228')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('captcha').send_keys('1111')
driver.find_element_by_id('login').click()
time.sleep(3)
#driver.find_element_by_id('navbar').click()
#driver.find_element_by_xpath("//a[@href='/second-kill/list']").click()
driver.implicitly_wait(10)
driver.find_element_by_link_text("微营销").click()
time.sleep(1)
driver.find_element_by_link_text("现金红包").click()
time.sleep(1)
driver.find_element_by_link_text("添加红包").click()
driver.implicitly_wait(5)
## Input Info
driver.find_element_by_xpath('//*[@id="main-container"]/div/div[2]/div[2]/div/div/div[2]/div[1]/form/div[3]/div/input').send_keys('Testslsl')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main-container"]/div/div[2]/div[2]/div/div/div[2]/div[1]/form/div[5]/div/input').send_keys('Remark:sls')
driver.find_element_by_xpath('//*[@id="money"]').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main-container"]/div/div[2]/div[2]/div/div/div[2]/div[1]/form/div[8]/div/input').send_keys('3')
time.sleep(2)
driver.find_element_by_link_text('保存').click()
time.sleep(5)
driver.close()

#driver.quit()

#driver.find_element_by_xpath("//div[@id='headactive']//a[@href='/second-kill/list']").click()


