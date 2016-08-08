# encoding: utf-8
import os
import unittest
from appium import webdriver
from time import sleep

desired_caps={
'platformName' : 'Android',
'platformVersion' : '5.0',
'deviceName' :  'Android Emulator',
'appPackage' : 'com.maishalei.seller',
'appActivity':  '.ui.activity.LauncherActivity',
'unicodeKeyboard':True,
'resetKeyboard':True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)
#driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
sleep(10)
#driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys(u"儿童")
sleep(1)
#driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys(66)
driver.press_keycode(66)

sleep(3)
driver.quit()