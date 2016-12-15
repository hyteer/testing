# encoding: utf-8
"""
微客多微信端并发测试脚本
Version:1.0
Author: YT

"""
import re
from locust import HttpLocust, TaskSet, task
import json
counter = 0

class UserBehavior(TaskSet):
    #global counter

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        res = self.client.get("/wkdianshang/oauth/testing?id=13764761", name=u"微信登录")
        print "Response status code:", res.status_code
        if res:
            self.count()

    def count(self):
        global counter
        counter += 1
        print "counter:%d" % counter

    '''
    @task(1)
    def index(self):
        res = self.client.get("/")
        if res:
            self.count_test()
    '''

    @task(1)
    def market_activity(self):
        res = self.client.post("/wkdianshang/market-activity/get-prize-ajax", {"id":1239,"shop_sub_id":0}\
            , name=u"大转盘活动")
        content = json.loads(res.content)        
        #errmsg = content["errmsg"]
        errcode = content["errcode"]
        print "Response status code:", res.status_code
        print("ResponseContent:%s", content)

        #matchs = re.search("teststr", content)
        #print "MatchResult:%s" % str(matchs)
        
        #print "errcode:%s,\nerrmsg:%s" % (errcode,str(errmsg))
        self.count()

        #print "Response status code:", res.status_code
        #print "Response content:", res.content



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 200
    max_wait = 500
    host = "http://wkdianshang.testnewwx.snsshop.net"
