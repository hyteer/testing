# coding: utf-8
import time,re
from selenium import webdriver

driver = webdriver.Chrome()


def login():
    driver.find_element_by_id('staff_id').send_keys('20170705')
    time.sleep(0.5)
    driver.find_element_by_id('password').send_keys('123456')
    time.sleep(0.8)
    driver.find_element_by_id('captcha').send_keys('11')
    time.sleep(0.5)
    driver.find_element_by_id('login').click()

def relogin():
    if driver.title == u"后台管理系统":
        login()
        time.sleep(2)
        driver.get('http://testwkdshopadmin.snsshop.net/terminal/list')


driver.get('http://testwkd.snsshop.net')
driver.implicitly_wait(10)
login()
driver.maximize_window()
time.sleep(2)
#driver.find_element_by_link_text('http://testwkdshopadmin.snsshop.net/terminal/list').click()
driver.find_element_by_link_text(u'微分店').click()

time.sleep(2)
driver.get('http://testwkdshopadmin.snsshop.net/terminal/basic-setting')
driver.get('http://testwkdshopadmin.snsshop.net/terminal/list')
driver.get('http://testwkdshopadmin.snsshop.net/terminal/product-list')

"""
PHPSESSID = driver.get_cookie('PHPSESSID')
cookies = driver.get_cookies()
csrf = driver.get_cookie('_csrf')


xpath = '''//meta[@name="csrf-token"]'''
#csrf = driver.find_element_by_xpath(xpath=xpath)
#print driver.page_source
#csrf_token = re.findall(r'(?<=name="csrf-token" content=").*(?===">)')
PHPSESSID['domain'] = 'testwkdshopadmin.snsshop.net'


new_PHPSESSID = PHPSESSID
new_cookies = {}
print "PHPSESSID:%s", PHPSESSID
#csrf = driver.get_cookie('_csrf')
#print "Title:%s,Cookie:%s" % (driver.title,cookie)
print "Cookies: ", cookies
for index,c in enumerate(cookies):
    print "domain:%s" % c['domain']
    if c['domain'] == "testwkd.snsshop.net":
        cookies[index]['domain'] = "testwkdshopadmin.snsshop.net"

for c in cookies:
    print "New_domain:%s" % c['domain']

driver.delete_all_cookies()



for new_cookie in cookies:
    print "newcooke:",new_cookie
    driver.add_cookie(new_cookie)

new_ss_cookies = driver.get_cookies()
print "New SS Cookies:", new_ss_cookies

#driver.get('http://testwkdshopadmin.snsshop.net/terminal/list')

#print "CSRF:%s" % csrf




'''
while True:
    #driver.get('http://testwkd.snsshop.net/tv-card-coupons/list')
    driver.get('http://testwkd.snsshop.net/hardware/device-response')
    print driver.title
    counter += 1
    time.sleep(1)
    print "Counter: %d" % counter
    driver.get('http://testwkdshopadmin.snsshop.net/agent/list')
    counter += 1
    print "Counter: %d" % counter
    time.sleep(1)
'''
"""
# driver.quit()