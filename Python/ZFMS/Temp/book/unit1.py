# encoding: utf-8
import unittest
import time
from selenium import webdriver
# from args import*
from args import elements, globalArgs
# import args

e = elements
g = globalArgs
HOME = g.HOME


class ZfmsLogin(unittest.TestCase):
    def setUp(self):
        # create a new firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        self.driver.get(HOME)
        driver.find_element_by_name(e.login_name).clear()
        driver.find_element_by_name(e.login_name).send_keys(g.username)
        driver.find_element_by_name(e.login_pass).clear()
        driver.find_element_by_name(e.login_pass).send_keys(g.password)
        driver.find_element_by_link_text('登录').click()

    def tearDown(self):
        url = self.driver.current_url
        print "URL: ", url
        self.assertEqual(g.HOME_LOGINED, url, 'URL checking failed')

        time.sleep(3)
        self.driver.quit()


'''
class ZfmsProcess(unittest.TestCase):
    def setUp(self):
        login = zfmsLogin(self)
        login.setUp()
        self.driver = webdriver.Firefox()

    def tempTest(self):
        driver = webdriver.Firefox()
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('tony')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('sa')
        driver.find_element_by_link_text('登录').click()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        '''


if __name__ == "__main__":
    unittest.main(verbosity=2)








