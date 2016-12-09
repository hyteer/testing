from locust import HttpLocust, TaskSet, task
import json

class UserBehavior(TaskSet):
    #global counter


    @task(1)
    def index(self):
        #self.client = HttpSession(base_url=self.host,)
        #self.client.headers={'debug':'YT','User-Agent':'Python'}
        self.client.headers={'User-Agent':'PythonYT'}
        res = self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    #min_wait = 1000
    #max_wait = 1500
