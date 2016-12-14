from locust import HttpLocust, TaskSet, task
import json

class UserBehavior(TaskSet):
    counter = 0
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        res = self.client.post("/login/login-ajax", {"username":"20160912", "password":"123456","captcha":"1"})
        print "Response status code:", res.status_code
        print "Response content:", res.content
        if res:
            self.count_test()

    def count_test(self):
        self.counter += 1
        print "counter:%d" % self.counter

    @task(2)
    def index(self):
        res = self.client.get("/")
        if res:
            self.count_test()

    @task(1)
    def member_list(self):
        res = self.client.post("/member/list-ajax", {"_page":1,"_page_size":20,"nickname":"","group_id":None,"shop_sub_id":"","agent_id":"","is_search":False,"belong_to_staff_id":"","createStart":"","createEnd":"","group_ids":[],"yestoday":False,"user_platform":0,"tags":[]})
        content = json.loads(res.content)
        errmsg = content["errmsg"]
        errcode = content["errcode"]
        print "errcode:%s,\nerrmsg:%s" % (errcode,str(errmsg))
        self.count_test()

        #print "Response status code:", res.status_code
        #print "Response content:", res.content

    @task(1)
    def second_kill_list(self):
        res = self.client.get("/second-kill/list")
        if res:
            self.count_test()



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 6000
