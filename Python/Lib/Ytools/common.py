# encoding: utf-8
import os
import time
import random


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

    def yt_decode(self,str1):
        # Decode bytes to string
        print "str:",str1
        str1.decode(encoding="utf-8", errors="strict")
        return str1

    def yt_to_string(self,args):
        # Convert the given args to string
        newstr = str(args)
        return newstr

    def yt_get_max(self,x,y):
        # Return the bigger one
        max1 = None
        if x == None:
            print "x is None."
        if y == None:
            print "y is None."
        if not str(x).strip():
            print "x is null"
            max = y
            return max
        if x >= y:
            max1 = x
        else:
            max1 = y
        return  max1
    def yt_get_max_sys(self,x,y):
        y = max(x,y)
        return y

    def yt_get_maxtime(self,time1,time2):
        # Compare two time string
        stamp1 = time.mktime(time.strptime(time1,'%Y-%m-%d %H:%M:%S'))
        stamp2 = time.mktime(time.strptime(time2,'%Y-%m-%d %H:%M:%S'))
        maxtime = max(stamp1,stamp2)
        if maxtime == stamp1:
            return time1
        else:
            return time2

    def yt_act_time_status(self,start_time):
        """ 通过活动开始时间与当前时间做比较，判断活动是否已开始

        返回值1=未开始，0=已开始

        """

        stamp = time.mktime(time.strptime(start_time,'%Y-%m-%d %H:%M:%S'))
        now = time.time()
        maxtime = max(stamp,now)
        #print "start time:",stamp
        #print "now:",now
        if maxtime == stamp:
            print "活动还未开始"
            return 1
        else:
            print "活动已经开始"
            return 0

    def yt_get_rand_integer(self,min,max):
        """ 产生一个随机整数
        :param min: 最小值
        :param max: 最大值
        :return:
        """
        min = int(min)
        max = int(max)
        rand = random.randint(min, max)
        return rand

    def yt_get_rand_float(self,minimum,maximum,digits,debug="False"):
        """ 产生一个随机浮点数

        :param minimum: 最小值
        :param maximum: 最大值
        :param digits: 位数
        :return:
        """
        min2 = float(minimum)
        max2 = float(maximum)
        digits2 = int(digits)

        if debug == "True":
            print "min:",min,"max:","digits:",digits
        rand = round(random.uniform(min2, max2), digits2)
        return rand

    def yt_screenshot(self,path="default"):
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



