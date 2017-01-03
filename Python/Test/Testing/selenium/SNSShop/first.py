
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://testnewwsh.snsshop.net/login/index')

print driver.title



time.sleep(2)

driver.quit()