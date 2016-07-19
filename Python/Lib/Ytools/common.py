# encoding: utf-8
import os
import time


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


