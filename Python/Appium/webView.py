#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
#desired_caps['platformVersion'] = '5.1.1'
#desired_caps['deviceName'] = 'Android Emulator'
desired_caps['deviceName'] = 'emulator-5554'
#desired_caps['deviceName'] = '7N2QXX145H032341'
desired_caps['appPackage'] = 'com.tencent.mm'
#desired_caps['appActivity'] = '.Calculator'
#desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver = webdriver.Remote('http://localhost:4491/wd/hub', desired_caps)

#delete = driver.find_element_by_id('del')

driver.implicitly_wait(20)
driver.find_element_by_id('com.tencent.mm:id/a_7').click()
time.sleep(2)
driver.quit()



#driver.find_element_by_android_uiautomator("1")
#driver.find_element_by_name("1").click()

time.sleep(20)

#driver.quit()