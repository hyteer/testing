# encoding: utf-8
from selenium import webdriver
import time

class ComWeb(object):
    def __init__(self):
        pass

    def getSlideArgsV(self,device):
        if device == 'small':   # 400x800
            hx1 = 240;hy1 = 580
            hx2 = 240;hy2 = 240
        if device == 'medium':
            hx1 = 350;hy1 = 950
            hx2 = 350;hy2 = 400
        if device == 'big':
            hx1 = 500;hy1 = 1400
            hx2 = 500;hy2 = 400
        return hx1,hy1,hx2,hy2

        print "hx1:%s,hx2:%s\nhx2:%s,hy2:%s"%(hx1,hy1,hx2,hy2)

    def getSlideArgsH(self,device):
        if device == 'small':   # 400x800
            hx1 = 350;hy1 = 500
            hx2 = 150;hy2 = 500
        if device == 'medium':   # Medium
            hx1 = 600;hy1 = 800
            hx2 = 180;hy2 = 800
        if device == 'big':   # Big
            hx1 = 900;hy1 = 1000
            hx2 = 300;hy2 = 1000

    def mytest2(self):
        print "mytest2..."

    def login(self,user,password,captcha):

        driver = webdriver.Chrome()
        driver.get('http://betanewwsh.vikduo.com/login/index')
        driver.find_element_by_id('staff_id').send_keys(user)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('captcha').send_keys(captcha)
        driver.find_element_by_id('login').click()
        time.sleep(3)
        driver.find_element_by_id('navbar').click()
        driver.find_element_by_xpath("//a[@href='/second-kill/list']").click()