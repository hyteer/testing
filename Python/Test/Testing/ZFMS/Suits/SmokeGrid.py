# encoding: utf-8
import sys
import unittest
import xmlrunner
from args import globalArgs
from Cases.org import user_grid
from Cases.form import table_grid

g = globalArgs


#g.setEnv('WINDOWS','chrome')
if len(sys.argv)>1:
    print "The length of argvs: " + str(len(sys.argv))
    br = sys.argv.pop()
    pf = sys.argv.pop()
    g.setEnv(pf, br)
    print "GET GLOB:" + str(g.getEnv())
else:
    g.setEnv('WINDOWS','firefox')

userTest = unittest.TestLoader().loadTestsFromTestCase(user_grid.ZfmsOrg)
tableTest = unittest.TestLoader().loadTestsFromTestCase(table_grid.ZfmsForm)
gridTest = unittest.TestSuite([userTest, tableTest])
xmlrunner.XMLTestRunner(verbosity=2,output='TestReports').run(gridTest)
#unittest.TextTestRunner(verbosity=2).run(userTest)


