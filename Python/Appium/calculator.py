#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
#desired_caps['platformVersion'] = '4.4.2'
desired_caps['platformVersion'] = '5.1.1'
#desired_caps['deviceName'] = 'Android Emulator'
desired_caps['deviceName'] = 'emulator-5554'
#desired_caps['deviceName'] = '7N2QXX145H032341'
desired_caps['appPackage'] = 'com.android.calculator2'
#desired_caps['appActivity'] = '.Calculator'
#desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#driver = webdriver.Remote('http://localhost:4492/wd/hub', desired_caps)

#delete = driver.find_element_by_id('del')

driver.find_element_by_id('digit8').click()
driver.find_element_by_id('mul').click()
driver.find_element_by_id('digit9').click()
driver.find_element_by_id('equal').click()
clr = driver.find_element_by_id('clear')
clr.click()
driver.quit()

#driver.find_element_by_android_uiautomator("1")
#driver.find_element_by_name("1").click()

time.sleep(20)

#driver.quit()