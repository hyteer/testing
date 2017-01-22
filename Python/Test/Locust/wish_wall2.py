# coding: utf-8
"""
共创辉煌活动并发测试脚本
Version:1.0
Author: YT

"""
import re
from locust import HttpLocust, TaskSet, task
import json,random,time,string

START_TIME = time.time()
TIME_ELAPSED = 0
GTIME = START_TIME

WX_DOMAIN = "http://wshtest.wkdwsh2099.m.vikduo.com/"
WX_ACC = "wshtest"
ACT_ID = "15132"
USER_ID = "18855458"


def randstr():
    return  string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')


counter = 0
ACT_ID = '2791'

class UserBehavior(TaskSet):
    #global counter

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        res = self.client.get("/NBwshtest/oauth/testing?id=13765003", name="微信登录")
        print "Response status code:", res.status_code
        if res:
            self.count()


    def count_total(self):
        global counter
        counter += 1
        print "counter:%d" % counter


    # 触发器
    def time_triger(self):
        global GTIME
        if GTIME <= time.time():
            GTIME += 4
            return True
        else:
            return False

    def console_log(self):
        print "Counter: %s" % str(counter)

    
    ################################# Transactions ####################################
    

    def chat_room_page(self):
        resp = self.client.get("/NBwshtest/wish-wall/show?id="+ACT_ID, name="聊天室页面")
        print "Response status code:", resp.status_code
        if resp:
            self.count()

    @task(1)
    def get_msglist(self):
        resp = self.client.post("/NBwshtest/wish-wall/list-by-floor-ajax", \
            {"activity_id":"${ACT_ID}","floor":randstr()}, name="消息列表")
        content = json.loads(resp.content)        

    @task(1)
    def send_wish(self):
        with self.client.post("/NBwshtest/wish-wall/send-msg-ajax", \
            {"activity_id":"${ACT_ID}","content":randstr()}, name="发送祝福",catch_response=True) as resp:
            
            self.count()

            if self.time_triger() == True:
                self.console_log()

            '''
            res = self.client.post("/NBwshtest/wish-wall/send-msg-ajax", \
                {"activity_id":"${ACT_ID}","content":randstr()}, name="发送祝福")

            '''
            content = json.loads(resp.content)        
            #errmsg = content["errmsg"]
            errcode = content["errcode"]
            if errcode != 0:
                print "errcode is: ", errcode
                resp.failure("Resp errcode is not 0. Resp content:",content)

            #print "Response status code:", res.status_code
            #print("ResponseContent:%s", content)

            #matchs = re.search("teststr", content)
            #print "MatchResult:%s" % str(matchs)
            
            #print "errcode:%s,\nerrmsg:%s" % (errcode,str(errmsg))
            #self.count()

            #print "Response status code:", res.status_code
            #print "Response content:", res.content



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
    host = "http://nbwshtest.testwkdwx.snsshop.net"
