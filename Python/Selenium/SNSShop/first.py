import unittest
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://betanewwsh.snsshop.net/login/index')

print driver.title



time.sleep(2)

driver.quit()