# encoding: utf-8
import os


class CommonUtils(object):

    def __init__(self):
       pass

    def mytest(self):        #此处为定义的keyword,可以在robotframework 中进行关键字测试。
        print "mytest"

    def printVersion(self):
        print u"【Ytools Library】 Version Number:1.0.1"

    def get_path(self,curdir,subdir):
        # Get a dir's path
        path = None
        if dir == None:
            path = curdir
        else:
            path = os.path.abspath(os.path.join(curdir, os.pardir, subdir))
        return path