# encoding: utf-8
class DemoModule(object):

    def __init__(self):
       pass

    def dm_test(self, test="a test"):
        print test
        return  "Test string: %s" % test