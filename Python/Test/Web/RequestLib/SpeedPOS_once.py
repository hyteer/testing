# coding:utf-8
import threading,time
import requests


def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''


str = "body=test1&cashierid=1&mch_id=1000000077&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no=10002000711177073802461811&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=31qdxsgvvb2yc3r2zcnure5o80l9hnpz"
url = "http://betagate.speedpos.snsshop.net/unifiedorder"
url2 = "http://10.100.100.88:16180/unifiedorder"

sign = md5(str)
sign2 = sign.upper()
print "md5:",sign2

xmldata = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>1000000077</mch_id><nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701</notify_url><openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>10002000711177073802461811</out_trade_no><return_url>http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee><trade_type>WXPAY.JSAPI</trade_type><sign>"+sign2+"</sign></xml>"
#r = requests.get(url)


counter = 0

def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

def req_speedpos(num):
    global counter
    r = requests.post(url2,data=xmldata)
    print 'Thread: %s' % num
    if r.status_code != 200:
        counter += 1
        print u"返回码：%s，总失败数：%d" % (r.status_code,counter)

    else:
        print r.content
    return r

threads = []
num = 5
# Call functions
def call_fun(fun,num):
    for i in range(num):
        t = threading.Thread(target=fun, args=(i,))
        threads.append(t)
        t.start()

#call_fun(worker,5)
#call_fun(req_speedpos,5)

for i in range(5):
    t = threading.Thread(target=req_speedpos, args=(i,))
    threads.append(t)
    t.start()
    time.sleep(0.5)
#req_speedpos()
