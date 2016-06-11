import sys

if len(sys.argv) >= 1:
    print "The length of argvs: " + str(len(sys.argv))
    i = 0
    print sys.argv.pop()
    print sys.argv.pop()
    print sys.argv.pop()
    print sys.argv.pop()
    #print sys.argv.pop(2)
    '''
    while i<= len(sys.argv):
        print sys.argv.pop()
        i = i+1
    '''
else:
    print "No argvs..."
'''
if __name__ == '__main__':
    #if len(sys.argv) > 1:
       # ZfmsOrg.PLATFORM = sys.argv.pop()
        #ZfmsOrg.BROWSER = sys.argv.pop()
    unittest.main(verbosity=2)
'''