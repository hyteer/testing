# -*- coding: utf-8 -*-
from locust import HttpLocust, TaskSet, task
from locust import web
import json, re, string, random, time

counter = 0
counter_success = 0
total_errors = 0
gtime = time.time()


url1 = "http://betagate.speedpos.snsshop.net/unifiedorder"
url = "http://10.100.100.88:16180/unifiedorder"
url3 = "http://10.100.100.82:16180/unifiedorder"

mch_list = (
    {"mch_id": "1000102875", "mch_key": "ycwth8umslsea4tmy0vhf3jhajzt3rfh"},    # for http://10.100.100.82:16180
    {"mch_id": "1000000069", "mch_key": "22m0fgxvbid1mjgpiq0vfyexwgayzzv1"},
    {"mch_id": "1000000070", "mch_key": "kpy5r160mq0p8idmjt0swj0vl6f4l6fm"},
    {"mch_id": "1000000072", "mch_key": "2bytm9n4ctekl36p3orf5eq6d657zmgn"},
    {"mch_id": "1000000073", "mch_key": "go5vof4cdab4xte4w46g55jljkluvldy"},
    {"mch_id": "1000000075", "mch_key": "ir1o3mpash1qj0kg2ocd1wubqowqq2kg"},
    {"mch_id": "1000000076", "mch_key": "0du7bqrj7m8y9y3goek972xh5vpf86pu"},
    {"mch_id": "1000000077", "mch_key": "31qdxsgvvb2yc3r2zcnure5o80l9hnpz"}
)
x = 0
mch_id = mch_list[x]['mch_id']
mch_key = mch_list[x]['mch_key']
#mch_key = "go5vof4cdab4xte4w46g55jljkluvldy" # 1000000073的key
#mch_key = "31qdxsgvvb2yc3r2zcnure5o80l9hnpz"    # 1000000077的ke

# MD5加密
def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

# 生成了随机数
def rand_num(x):
    randNameX = string.join(random.sample(['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9'], x)).replace(" ","")
    return randNameX

# 生成随机out_trade_no
def rand_out_trade_no():
    rand_no = rand_num(18)
    out_trade_no = "10002000" + rand_no
    #print "out_trade_no: %s" % out_trade_no
    return out_trade_no

# 生成XML数据
def get_xmldata(mch_id,mch_key):
    out_trade_no = rand_out_trade_no()
    '''
    str = "body=test1&cashierid=1&mch_id="+mch_id+"&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=\
http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&\
openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no="+out_trade_no+"&\
return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&\
spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key="+mch_key
'''


    str = "body=test1&cashierid=1&mch_id={mch_id}&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=\
http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&\
openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no={out_trade_no}&\
return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&\
spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key={mch_key}".format(mch_id=mch_id,out_trade_no=out_trade_no,mch_key=mch_key)

    str2 = "body=test1&cashierid=1&mch_id="+mch_id+"&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&\
notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&\
openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no="+out_trade_no+"&\
return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&\
spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key="+mch_key

    sign = md5(str)
    sign2 = sign.upper()

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

    return xmldata



class UserBehavior(TaskSet):
    #global counter

    # 计数器
    def count_success(self):
        global counter_success
        counter_success += 1

    def count_total(self):
        global counter,counter_success,total_errors
        counter += 1

    # 输出控制台日志
    def console_log(self):
        global counter,counter_success,total_errors
        total_errors = counter-counter_success
        if total_errors == 0:
            err_rate = float(0.0)
        else:
            err_rate = total_errors/float(counter)
        err_rate_perc = round(err_rate*100,1)
        print u"Total:%d, Success:%d, Errors:%d, ErrorRate:%s%%" % (counter,counter_success,total_errors,str(err_rate_perc))

    # 触发器
    def time_triger(self):
        global gtime
        if gtime <= time.time():
            gtime += 4
            return True
        else:
            return False

    # 任务：支付接口
    @task(1)
    def unified_order(self):
        xmldata = get_xmldata(mch_id,mch_key)
        if self.time_triger() == True:
            self.console_log()


        with self.client.post("/unifiedorder", data=xmldata,catch_response=True) as response:
            self.count_total()

            if response.status_code == 200:

                if response.content is False:
                    response.failure("No Response Content.")

                elif response.content == None:
                        response.failure("Response is null.")
                else:
                    content = response.content.decode("UTF-8")
                    #print u"Response status code:", response.status_code
                    #print u"Response content:", content
                    #matchs = re.search("SUCCESS", content)
                    matchs = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",content)
                    #matchs2 = re.findall(r"(?<=<retcode>).*(?=<\/retcode>)",content)
                    #print matchs
                    if len(matchs):
                        if matchs[0] == "SUCCESS":
                            response.success()
                            self.count_success()
                        else:
                            response.failure(u"Response not success, retmsg: %s" % matchs[0])
                            print u"Response content:", content
                    elif content and content != "":
                        response.failure("Asert Error: %s." % content)
                    else:
                        response.failure("No Response Content!")

            else:
                response.failure(u"Got wrong response, response code: %r,Content:%r" %(response.status_code,response.text))

        '''
        res = self.client.post("/unifiedorder", xmldata2)
        content = res.content.decode("UTF-8")
        matchs = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",content)
        '''


@web.app.route("/info")
def test_info():
    global counter,counter_success,total_errors
    total_errors = counter-counter_success
    if total_errors == 0:
        err_rate = float(0.0)
    else:
        err_rate = total_errors/float(counter)
    err_rate_perc = round(err_rate*100,1)
    return "Total:%d, Success:%d, Errors:%d, ErrorRate:%s%%" % (counter,counter_success,total_errors,str(err_rate_perc))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 6000
