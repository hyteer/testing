from locust import HttpLocust, TaskSet, task
import re


class UserBehavior(TaskSet):
    #global counter

    
    @task(1)
    def index(self):
        with self.client.post("/", catch_response=True) as response:
        
            content = response.content.decode("UTF-8")
            matchs = re.search("hello", content)
            assert matchs is not None


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
    host = "http://gaea.demo.cc"
