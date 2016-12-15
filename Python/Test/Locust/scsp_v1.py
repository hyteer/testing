# -*- coding: utf-8 -*-
from locust import HttpLocust, TaskSet, task, events
from locust import web
import json, re, string, random, time

counter = 0
counter_success = 0
total_errors = 0
start_time = time.time()
time_elapsed = 0

counter_start = 0
counter_case = 0

errors_start = 0
errors_case = 0
success_start = 0
success_case = 0

this_time_start = 0
this_time_end = 0
this_time_cost = 0
last_time_cost = 0

last_case = 0
last_errors = 0

master_counter_start = 0
master_counter_case = 0



gtime = start_time
err = ""
err2 = ""
debug_mode = 0
""" 
    《Debug模式说明》
    0:非调试模式，对返回数据做完整校验
    1:调试模式1(只要返回200则标记成功)
    2:调试模式2（检查返回包是否为空）
    3:调试模式3（检查返回包中是否有成功标志，不做其它数据校验）

"""


#url_beta = "http://betagate.speedpos.snsshop.net/unifiedorder"
url = "http://gate.speedpos.cn:8181/unifiedorder"
#url_dev = "http://10.100.100.82:16180/unifiedorder"

mch_list = (
    {"mch_id": "1000102875", "mch_key": "ycwth8umslsea4tmy0vhf3jhajzt3rfh"},    # for http://10.20.60.76:17180/unifiedorder
    {"mch_id": "1000000001", "mch_key": "but15ozu7ckfqfn1ksle541rbatskk3x"},    # for http://gate.speedpos.cn
    {"mch_id": "1000102875", "mch_key": "ycwth8umslsea4tmy0vhf3jhajzt3rfh"},    # for http://10.100.100.82:16180
    {"mch_id": "1000000069", "mch_key": "22m0fgxvbid1mjgpiq0vfyexwgayzzv1"},    # for http://betagate.speedpos.snsshop.net
    {"mch_id": "1000000070", "mch_key": "kpy5r160mq0p8idmjt0swj0vl6f4l6fm"},
    {"mch_id": "1000000072", "mch_key": "2bytm9n4ctekl36p3orf5eq6d657zmgn"},
    {"mch_id": "1000000073", "mch_key": "go5vof4cdab4xte4w46g55jljkluvldy"},
    {"mch_id": "1000000075", "mch_key": "ir1o3mpash1qj0kg2ocd1wubqowqq2kg"},
    {"mch_id": "1000000076", "mch_key": "0du7bqrj7m8y9y3goek972xh5vpf86pu"},
    {"mch_id": "1000000077", "mch_key": "31qdxsgvvb2yc3r2zcnure5o80l9hnpz"}
)
x = 5
mch_id = mch_list[x]['mch_id']
mch_key = mch_list[x]['mch_key']

############################################ Helper Functions #############################################
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
    global debug_mode
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
spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key={mch_key}".format\
(mch_id=mch_id,out_trade_no=out_trade_no,mch_key=mch_key)

    '''
    str2 = "body=test1&cashierid=1&mch_id="+mch_id+"&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&\
notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&\
openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no="+out_trade_no+"&\
return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&\
spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key="+mch_key
    '''

    sign = md5(str)
    sign_upper = sign.upper()

    xmldata = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>"+mch_id+"</mch_id>\
<nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>\
http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701</notify_url>\
<openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>"+out_trade_no+"</out_trade_no>\
<return_url>http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701\
</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee>\
<trade_type>WXPAY.JSAPI</trade_type><sign>"+sign_upper+"</sign></xml>"

    xmldata_debug = '0'

    '''
    xmldata2 = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>"+mch_id+"</mch_id>\
<nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>\
http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701</notify_url>\
<openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>"+out_trade_no+"</out_trade_no>\
<return_url>http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701\
</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee>\
<trade_type>WXPAY.JSAPI</trade_type><sign>"+sign_upper+"</sign></xml>"
    '''

    if debug_mode == 2:
        return xmldata_debug
    else:
        return xmldata



####################################### Event hooks defination ############################################
'''
def on_request_failure(request_type, name, response_time, exception):
    print 'Type: %s, Name: %s, Time: %fms, Reason: %r' % \
            (request_type, name, response_time, exception)

def on_locust_error(locust_instance, exception, tb):
    print "%r, %s, %s" % (locust_instance, exception, "".join(traceback.format_tb(tb)))

def on_hatch_complete(user_count):
    print "Haha, Locust have generate %d users" % user_count
'''

def on_master_start_hatching():
    global counter,master_counter_start
    master_counter_start = counter
    print("new test starts, master counter start at:%s" % master_counter_start)


def on_master_stop_hatching():
    global counter,master_counter_start,master_counter_case
    master_counter_case = counter - master_counter_start
    print("new test case master count:%s" % counter_case)

def on_locust_start_hatching():
    global counter,counter_start, counter_success, errors_start,counter_case,errors_case,\
    last_case,last_errors,this_time_start,this_time_cost,last_time_cost
    counter_start = counter
    this_time_start = time.time()
    errors_start = counter - counter_success
    last_case = counter_case
    last_errors = errors_case
    last_time_cost = this_time_cost
    counter_case = "waiting..."
    errors_case = "waiting..."
    this_time_cost = "waiting..."
    print("new test starts, counter start:%s,errors start:%s" % (counter_start,errors_start))

def on_locust_stop_hatching():
    #time.sleep(1)
    global counter,counter_start,counter_case, counter_success, errors_case, errors_start, this_time_start\
    ,this_time_cost,this_time_end
    counter_case = counter - counter_start
    this_time_end = time.time()
    this_time_cost = int(this_time_end - this_time_start)
    errors_case = counter - counter_success - errors_start


    print("new test case count:%s,errors:%s" % (counter_case,errors_case))

def on_hatch_complete(user_count):
    print "Haha, Locust have generate %d users" % user_count


#events.request_failure += on_request_failure
#events.locust_error += on_locust_error
#events.hatch_complete += on_hatch_complete
events.master_start_hatching += on_master_start_hatching
events.master_stop_hatching += on_master_stop_hatching
events.locust_start_hatching += on_locust_start_hatching
events.locust_stop_hatching += on_locust_stop_hatching


########################################### Loadtesting ##################################################

class UserBehavior(TaskSet):
    #global counter

    # 计数器
    def count_success(self):
        global counter,counter_success,total_errors
        counter_success += 1
        total_errors = counter - counter_success

    

    def count_total(self):
        global counter,counter_success,total_errors
        counter += 1

    # 输出控制台日志
    def console_log(self):
        global counter,counter_success,total_errors,err,start_time, time_elapsed
        #total_errors = counter-counter_success
        if total_errors == 0:
            err_rate = float(0.0)
        else:
            err_rate = total_errors/float(counter)
        err_rate_perc = round(err_rate*100,1)
        #print "err:%s" % err
        print u"Elapsed:%s, Info:Total:%d, Success:%d, Errors:%d, ErrRate:%s%%" % (time_elapsed,counter,\
            counter_success,total_errors,str(err_rate_perc))

    # 触发器
    def time_triger(self):
        global gtime
        if gtime <= time.time():
            gtime += 4
            return True
        else:
            return False
    def count_time(self):
        global time_elapsed
        time_now = time.time()
        time_elapsed = int(time_now - start_time)



    # 任务：支付接口
    @task(1)
    def unified_order(self):
        global err,err2, debug_mode
        xmldata = get_xmldata(mch_id,mch_key)
        if self.time_triger() == True:
            self.console_log()

        def order_debug_mode1():
            if response.status_code == 200:
                response.success()
                self.count_success()

        def order_debug_mode2():
            if response.status_code == 200:

                if response.content is False:
                    response.failure("No Response Content.")

                elif response.content is None:
                    response.failure("Response Content is None.")
                elif response.content == "":
                    response.failure("Reponse Content is null")
                else:
                    response.success()
                    self.count_success()
            else:
                response.failure(u"Got wrong response, response code: %r,Content:%r" %(response.status_code,response.text))

        def order_debug_mode3():
            if response.status_code == 200:

                if response.content is False:
                    response.failure("No Response Content.")

                elif response.content is None:
                    response.failure("Response Content is None.")
                elif response.content == "":
                    response.failure("Reponse Content is null")
                else:
                    content = response.content
                    match = re.search(r"<xml>",content)
                    if match is not None:
                        response.success()
                        self.count_success()
                    else:
                        response.failure("Reponse error, content:%s" % content)              
            else:
                response.failure(u"Got wrong response, response code: %r,Content:%r" %(response.status_code,response.text))

        def order_normal_mode():
            if response.status_code == 200:

                if response.content is False:
                    response.failure("No Response Content.")

                elif response.content is None:
                    response.failure("Response Content is None.")
                elif response.content == "":
                    response.failure("Reponse Content is null")
                else:
                    content = response.content.decode("UTF-8")
                    #restext = response.text.decode("UTF-8")
                    #print u"Response status code:", response.status_code
                    #print u"Response content:", content
                    matchs = re.search("SUCCESS", content)
                    matchs_msg = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",content)
                    #matchs = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",content)
                    #matchs2 = re.findall(r"(?<=<retcode>).*(?=<\/retcode>)",content)
                    #print matchs
                    if len(matchs_msg):
                        if matchs_msg[0] == "SUCCESS":
                            response.success()
                            self.count_success()
                        else:
                            response.failure("Asert Error: %s." % content)
                            matchs_code = re.findall(r"(?<=<retcode>).*(?=<\/retcode>)",content)
                            err = "retcode:%s,retmsg:%s" % (matchs_code[0], matchs_msg[0])                          

            else:
                response.failure(u"Got wrong response, response code: %r,Content:%r" %(response.status_code,response.text))

        # 开始请求

        with self.client.post("/unifiedorder", data=xmldata,catch_response=True) as response:
            self.count_total()
            if debug_mode == 1:
                order_debug_mode1()
            elif debug_mode == 2:
                order_debug_mode2()

            elif debug_mode == 3:
                order_debug_mode3()

            else:
                order_normal_mode()
            

        self.count_time()    # count elapsed time        

        '''
        res = self.client.post("/unifiedorder", xmldata2)
        content = res.content.decode("UTF-8")
        matchs = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",content)
        '''


@web.app.route("/info")
def test_info():
    global mch_id,counter,counter_success,total_errors,start_time,time_elapsed,counter_case,errors_case,\
    last_case,last_errors,this_time_start,this_time_cost,last_time_cost
    #total_errors = counter-counter_success
    '''
    time_now = time.time()
    elapsed = int(time_now - start_time)
    '''
    '''
    if total_errors == 0:
        err_rate = float(0.0)
    else:
        err_rate = total_errors/float(counter)
    err_rate_perc = round(err_rate*100,1)
    if err != "":
        err = "Total:%s,Elapsed:%s, info:%s" % (counter, str(time_elapsed), err)
    else:
        err = "Total:%s, Elapsed:%s<br>Info:No assertion error." % (counter, time_elapsed)
    return err
    '''
    total_info = "<h3>Total</h3>Samples:%s,Elapsed:%s, Success:%s, Errors:%s" % \
    (counter, str(time_elapsed), counter_success,total_errors)
    last_info =  "<h3>Last Test</h3>Samples:%s,Elapsed:%s,Errors:%s" % (last_case, last_time_cost,last_errors)
    this_info = "<h3>This Test</h3>Samples:%s,Elapsed:%s,Errors:%s<br><br>StartTime:%s,EndStime:%s" % \
    (counter_case, this_time_cost,errors_case,this_time_start,this_time_end)
    return "<h3>mch_id:%s</h3>%s%s%s" % (mch_id,total_info,last_info,this_info)

    '''
    return "<h3>Total</h3>Samples:%s,Elapsed:%s, Success:%s, Errors:%s<h3>This time</h3>\
    Samples:%s, Errors:%s" % \
    (counter, str(time_elapsed), counter_success,total_errors, counter_case, errors_case)
    #return "测试数据\nTotal:%d, Success:%d, Errors:%d, ErrorRate:%s%%" % (counter,counter_success,total_errors,str(err_rate_perc))
    '''




class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 10
