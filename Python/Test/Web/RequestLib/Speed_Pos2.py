import requests,string,random
from requests import HTTPError,ConnectionError,Timeout

def RateLimitExceeded():
    return False


def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

def rand_num(x):
    randNameX = string.join(random.sample(['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9'], x)).replace(" ","")
    return randNameX


'''
str = "body=test1&cashierid=1&mch_id=1000000077&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no=10002000711177073802461811&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=31qdxsgvvb2yc3r2zcnure5o80l9hnpz"
str2 = "body=test1&cashierid=1&mch_id=1000000077&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://10.100.100.88:16180/notify/1000100001/1000100001201611021915213701&openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no=10002000711177073802461811&return_url=http://10.100.100.88:16180/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=31qdxsgvvb2yc3r2zcnure5o80l9hnpz"
url = "http://betagate.speedpos.snsshop.net/unifiedorder"
url2 = "http://10.100.100.88:16180/unifiedorder"

sign = md5(str)
sign2 = sign.upper()
print "md5:",sign2

xmldata = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>1000000077</mch_id><nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701</notify_url><openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>10002000711177073802461811</out_trade_no><return_url>http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee><trade_type>WXPAY.JSAPI</trade_type><sign>"+sign2+"</sign></xml>"
xmldata2 = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>1000000077</mch_id><nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>http://10.100.100.88:16180/notify/1000100001/1000100001201611021915213701</notify_url><openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>10002000711177073802461811</out_trade_no><return_url>http://10.100.100.88:16180/success/1000100001/1000100001201611021915213701</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee><trade_type>WXPAY.JSAPI</trade_type><sign>"+sign2+"</sign></xml>"
#r = requests.get(url)
'''


url = "http://betagate.speedpos.snsshop.net/unifiedorder"
url2 = "http://10.100.100.88:16180/unifiedorder"
mch_id = "1000000073"
mch_key = "go5vof4cdab4xte4w46g55jljkluvldy"
#mch_key = "31qdxsgvvb2yc3r2zcnure5o80l9hnpz"

def rand_out_trade_no():
    rand_no = rand_num(18)
    out_trade_no = "10002000" + rand_no
    print "out_trade_no",out_trade_no
    return out_trade_no

#out_trade_no = rand_out_trade_no()

def get_xmldata(mch_id,mch_key):
    out_trade_no = rand_out_trade_no()
    #print "out_trade_no:",out_trade_no
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
    print str
    print xmldata
    return xmldata2

xmldata = get_xmldata(mch_id,mch_key)

try:
    r = requests.post(url2,data=xmldata)
    print r.status_code,r.content
except (HTTPError, ConnectionError, Timeout, RateLimitExceeded) as e:
    print e
    pass
except Exception as e:
    raise


'''
i = 1
max = 5
while i < max:
    res = requests.post(url2,data=xmldata2)
    print res.status_code,res.content
    i += 1
'''