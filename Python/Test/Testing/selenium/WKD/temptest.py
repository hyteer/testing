
import time
from selenium import webdriver

driver = webdriver.Chrome()

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

counter = 0

while True:
    #driver.get('http://testwkd.snsshop.net/tv-card-coupons/list')
    driver.get('http://testwkd.snsshop.net/hardware/device-response')
    print driver.title
    counter += 1
    print "Counter: %d" % counter
    time.sleep(2)

# driver.quit()