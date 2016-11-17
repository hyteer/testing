# -*- coding: utf-8 -*-
from locust import HttpLocust, TaskSet, task
import json,re

counter = 0

def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

url = "http://betagate.speedpos.snsshop.net/unifiedorder"
url2 = "http://10.100.100.88:16180/unifiedorder"
mch_id = "1000000073"
mch_key = "go5vof4cdab4xte4w46g55jljkluvldy"
#mch_key = "31qdxsgvvb2yc3r2zcnure5o80l9hnpz"
out_trade_no = "10002000762646726243476010"

str = "body=test1&cashierid=1&mch_id="+mch_id+"&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=\
http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&\
openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no="+out_trade_no+"&\
return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&\
spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key="+mch_key

str2 = "body=test1&cashierid=1&mch_id="+mch_id+"&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&\
notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&\
openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no="+out_trade_no+"&\
return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&\
spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key="+mch_key


sign = md5(str)
sign2 = sign.upper()
#print "md5:",sign2

xmldata = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>"+mch_id+"</mch_id>\
<nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>\
http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701</notify_url>\
<openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>"+out_trade_no+"</out_trade_no>\
<return_url>http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701\
</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee>\
<trade_type>WXPAY.JSAPI</trade_type><sign>"+sign+"</sign></xml>"

xmldata2 = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>"+mch_id+"</mch_id>\
<nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>\
http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701</notify_url>\
<openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>"+out_trade_no+"\
</out_trade_no><return_url>http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701\
</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee>\
<trade_type>WXPAY.JSAPI</trade_type><sign>"+sign2+"</sign></xml>"



class UserBehavior(TaskSet):
    #global counter

    def count_test(self):
        global counter
        counter += 1
        print "counter:%d" % counter

    @task(1)
    def unified_order(self):
        
        with self.client.post("/unifiedorder", data=xmldata2,catch_response=True) as response:

            if response:
                content = response.content.decode("UTF-8")
                print u"Response status code:", response.status_code
                print u"Response content:", content
                matchs = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",content)
                self.count_test()
                if not matchs[0] or matchs[0] != "SUCCESS":
                    response.failure("Got wrong response")

        '''
        res = self.client.post("/unifiedorder", xmldata2)
        content = res.content.decode("UTF-8")
        matchs = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",content)
        '''





class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 6000
