# -*- coding: utf-8 -*-

class runEnv():
    PLATFORM = "no platform"
    BROWSER = "no browser"
    def setPlatform(self,platform):
        #self.PLATFORM = platform  用self则设置的是实例的变量值而不是类的变量值
        runEnv.PLATFORM = platform  # 设置类变量的值

def setBrowser(browser):
    runEnv.BROWSER = browser
def getBrowser():
    return runEnv.BROWSER

