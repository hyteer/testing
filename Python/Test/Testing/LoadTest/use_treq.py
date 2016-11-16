#!/usr/bin/env python
from twisted.internet import epollreactor
epollreactor.install()

from twisted.internet import reactor, task
from twisted.web.client import HTTPConnectionPool
import treq
import random
from datetime import datetime

req_generated = 0
req_made = 0
req_done = 0

str = "body=test1&cashierid=1&mch_id=1000000077&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no=10002000711177073802461811&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=31qdxsgvvb2yc3r2zcnure5o80l9hnpz"
url = "http://betagate.speedpos.snsshop.net/unifiedorder"


def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''


sign = md5(str)
sign2 = sign.upper()
post_data = "<xml><body>test1</body><cashierid>1</cashierid><mch_id>1000000077</mch_id><nonce_str>xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn</nonce_str><notify_url>http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701</notify_url><openid>odLjYvwUYEEq1HMGQY_3CErEGLSU</openid><out_trade_no>10002000711177073802461811</out_trade_no><return_url>http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701</return_url><spbill_create_ip>127.0.0.1</spbill_create_ip><total_fee>1</total_fee><trade_type>WXPAY.JSAPI</trade_type><sign>"+sign2+"</sign></xml>"

cooperator = task.Cooperator()

pool = HTTPConnectionPool(reactor)

def counter():
  '''This function gets called once a second and prints the progress at one
  second intervals.
  '''
  global req_generated,req_made,req_done
  print("Requests: {} generated; {} made; {} done".format(req_generated, req_made, req_done))
  print req_generated
  # reset the counters and reschedule ourselves
  req_generated = req_made = req_done = 0
  reactor.callLater(1, counter)

def body_received(body):
  global req_done
  req_done += 1

def request_done(response):
  global req_made
  deferred = treq.json_content(response)
  req_made += 1
  deferred.addCallback(body_received)
  deferred.addErrback(lambda x: None) # ignore errors
  return deferred

def request():
  res = treq.post(url=url,data=post_data,pool=pool)
  return res

def requests_generator():
  global req_generated
  while True:
    deferred = request()
    req_generated += 1
    # do not yield deferred here so cooperator won't pause until
    # response is received
    yield None

if __name__ == '__main__':
  # make cooperator work on spawning requests
  cooperator.cooperate(requests_generator())

  # run the counter that will be reporting sending speed once a second
  reactor.callLater(1, counter)

  # run the reactor
  reactor.run()