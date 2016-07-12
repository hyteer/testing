# encoding: utf-8
import os


class CommonUtils(object):

    def __init__(self):
       pass

    def yt_mytest(self):        #此处为定义的keyword,可以在robotframework 中进行关键字测试。
        print "mytest"

    def yt_printVersion(self):
        print u"【Ytools Library】 Version Number:1.0.1"

    def yt_get_parpath(self,curdir,subdir):
        # Get a dir's path
        path = None
        if dir == None:
            path = curdir
        else:
            path = os.path.abspath(os.path.join(curdir, os.pardir, subdir))
        return path

    def yt_decode(self,str):
        # Decode bytes to string
        print "str:",str
        str.decode(encoding="utf-8", errors="strict")
        return str



