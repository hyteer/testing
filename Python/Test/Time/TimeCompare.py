 # encoding: utf-8
import time

def yt_act_time_status(start_time):
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

starttime = "2016-08-01 09:56:26"
yt_act_time_status(starttime)