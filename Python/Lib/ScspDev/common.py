# encoding: utf-8
import sys as mysys
reload(mysys)
mysys.setdefaultencoding('utf-8')

import os
import time
import random
from version import VERSION
import hashlib
import types


class CommonUtils(object):

    def __init__(self):
       pass

    def sp_test(self, test="a test"):        #此处为定义的keyword,可以在robotframework 中进行关键字测试。
        print test
        return  "Test string: %s" % test

    def sp_version(self):
        """
        打印版本
        """
        print u"【Ytools Library】Version:%s" % VERSION
        return VERSION

 

    def yt_screenshot(self,path="default"):
        """
        说明：截图保存在 C:\Temp\

        """
        import wx
        from datetime import datetime
        now = datetime.now()
        strnow = now.strftime("%Y%m%d_%H%M%S_") + str(now.microsecond)

        app = wx.App()  # Need to create an App instance before doing anything
        screen = wx.ScreenDC()
        size = screen.GetSize()
        bmp = wx.EmptyBitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem  # Release bitmap
        bmp.SaveFile('C:\\Temp\\'+strnow+'.png', wx.BITMAP_TYPE_PNG)
        print "Taking screenshot success."

    def yt_md5(self, mystr):
        """
        说明：MD5加密
        """
        print "your string:%s" % mystr
        m = hashlib.md5()
        m.update(mystr)
        md5_str = m.hexdigest()
        print "encryped string:%s" % md5_str

        """
        if type(mystr) is types.StringType:
            m = hashlib.md5()
            m.update(mystr)
            md5_str = m.hexdigest()
            print "encryped string:%s" % md5_str
            return md5_str

        else:
            return ''
        """
        return md5_str


class Ytools2(object):

    def __init__(self):
       pass