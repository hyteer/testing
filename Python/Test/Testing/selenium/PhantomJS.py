# coding: utf-8
import time
from selenium import webdriver

#driver = webdriver.Chrome()
#driver = webdriver.PhantomJS(executable_path='D:\\Tool\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver = webdriver.PhantomJS()

driver.get('http://testwkd.snsshop.net')
driver.implicitly_wait(10)
driver.find_element_by_id('staff_id').send_keys('20170705')
time.sleep(0.5)
driver.find_element_by_id('password').send_keys('123456')
time.sleep(0.8)
driver.find_element_by_id('captcha').send_keys('11')
time.sleep(0.5)
driver.find_element_by_id('login').click()
driver.maximize_window()

time.sleep(2)
print "Title:%s" % driver.title
assert driver.title == u"概况"
driver.get('http://testwkd.snsshop.net/hardware/device-response')
time.sleep(2)
print "Title:%s" % driver.title
driver.get('http://testwkd.snsshop.net/second-kill/list')
print "Title:%s" % driver.title
counter = 0

time.sleep(3)
'''
while True:
    #driver.get('http://testwkd.snsshop.net/tv-card-coupons/list')
    driver.get('http://testwkd.snsshop.net/hardware/device-response')

    driver.switch_to.window(1)
    print driver.title
    counter += 1
    print "Counter: %d" % counter
    time.sleep(2)
'''

# driver.quit()