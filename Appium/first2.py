#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
#desired_caps['deviceName'] = 'Android Emulator'
desired_caps['deviceName'] = 'emulator-5554'
#desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('clear').click()
driver.find_element_by_id('digit8').click()
driver.find_element_by_id('mul').click()
driver.find_element_by_id('digit9').click()
driver.find_element_by_id('equal').click()

#driver.find_element_by_android_uiautomator("1")
#driver.find_element_by_name("1").click()

time.sleep(20)

#driver.quit()