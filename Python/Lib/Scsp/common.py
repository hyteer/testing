# encoding: utf-8
import os
import time
import random
from version import VERSION


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
        print "【Ytools Library】Version:%s" % VERSION

 

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
        import hashlib
        import types
        if type(mystr) is types.StringType:
            m = hashlib.md5()
            m.update(mystr)
            return m.hexdigest()
        else:
            return ''


class Ytools2(object):

    def __init__(self):
       pass