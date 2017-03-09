# coding: utf-8
from locust import HttpLocust, TaskSet, task
import re,random,string
from urllib import unquote,urlencode,quote_plus


class UserBehavior(TaskSet):
    #global counter
    def get_url(self):
        param1 = string.join(random.sample(['1','2','3','4','5','6','7','8','9'], 5)).replace(" ","")
        param2 = string.join(random.sample(['1','2','3','4','5','6','7','8','9'], 2)).replace(" ","")
        param3 = str(random.randrange(1,3))
        params = param1 + ',' + param2 + ',' + param3
        quoteUrl=quote_plus(url,safe=':\'/?&=()%')
        url = '/collect/index?id=1&siteid=686&param='+',/second-kill/list&lg=zh-cn&showp=1920x1080&page=http://testwkd.snsshop.net/second-kill/list&uri=testwkd.snsshop.net/second-kill/list&title=%%E7%%A7%%92%%E6%9D%%80%%E6%%B4%%BB%%E5%8A%%A8%%E7%%AE%%A1%%E7%%90%86&key=&fromkey=&vid=&agent=Mozilla/5.0%20(Windows%20NT%206.1;%20WOW64)%20AppleWebKit/537.36%20(KHTML,%%20like%%20Gecko)%20Chrome/52.0.2743.6%20Safari/537.36&referrer=http://testwkd.snsshop.net/&rnd=1608197300'
        #url = urlencode(url_raw)

        return url         
    
    @task(1)
    def index(self):
        url = self.get_url()
        print url
        with self.client.post(url, catch_response=True,name='Ta_Req') as response:
            if response.status_code == 200:

                if response.content is False:
                    response.failure("No Response Content.")

                elif response.content is None:
                    response.failure("Response Content is None.")
                elif response.content == "":
                    response.failure("Reponse Content is null")
                else:
                    content = response.content.decode("UTF-8")
                    matchs = re.search("1", content)
                    assert matchs is not None
                    response.success()
                    
            else:
                response.failure(u"Got wrong response, response code: %r,Content:%r" %(response.status_code,response.text))
            
            
            


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 2000
    host = "http://betata.snsshop.net"
