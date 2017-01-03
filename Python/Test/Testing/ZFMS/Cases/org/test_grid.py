import sys
import unittest
import xmlrunner
from args import globalArgs
import user_test

g = globalArgs


#g.setGlb('WINDOWS','chrome')
if len(sys.argv)>1:
    print "The length of argvs: " + str(len(sys.argv))
    br = sys.argv.pop()
    pf = sys.argv.pop()
    g.setGlb(pf, br)
    print "GET GLOB:" + str(g.getGlb())
else:
    g.setGlb('WINDOWS','firefox')

userTest = unittest.TestLoader().loadTestsFromTestCase(user_test.ZfmsOrg)
xmlrunner.XMLTestRunner(verbosity=2,output='TestReports').run(userTest)
#unittest.TextTestRunner(verbosity=2).run(userTest)


