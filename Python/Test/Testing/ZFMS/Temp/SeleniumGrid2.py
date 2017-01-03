# -*- coding: utf-8 -*-
# This script for demonstrate Selenium Grid distribute testing
import unittest
import xmlrunner
import time
import sys

from selenium import webdriver
from args import globalArgs, elements
from Cases.form import table
from Cases.org import user_grid

reload(sys)
sys.setdefaultencoding('utf-8')

g = globalArgs
e = elements


#formTest = unittest.TestLoader().loadTestsFromTestCase(table.ZfmsForm)
#smokeTest = unittest.TestSuite([userTest, formTest])
# unittest.TextTestRunner(verbosity=2).run(suite)

# xmlrunner.XMLTestRunner(verbosity=2,output='TestReports').run(userTest)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        browser = sys.argv.pop()
        platform = sys.argv.pop()
        g.setBrowser(browser)
        g.setPlatform(platform)
        print "Browser: " + g.getBrowser()
        print "Platform: " + g.getPlatform()
    user_grid.getGlb()
    #userTest = unittest.TestLoader().loadTestsFromTestCase(user_grid.ZfmsOrg)
    #unittest.main(xmlrunner.XMLTestRunner(verbosity=2, output='TestReports').run(userTest))

'''
if __name__ == '__main__':
    #if len(sys.argv) > 1:
       # ZfmsOrg.PLATFORM = sys.argv.pop()
        #ZfmsOrg.BROWSER = sys.argv.pop()
    unittest.main(verbosity=2)
'''




