import md5

# 1. Use MD5 lib
src = 'this is a md5 test.'
sign_str = "body=test1&cashierid=1&mch_id=1000000073&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=odLjYvwUYEEq1HMGQY_3CErEGLSU&out_trade_no=10002000028431493853215647&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=go5vof4cdab4xte4w46g55jljkluvldy"
m1 = md5.new()   
m1.update(sign_str)
print m1.hexdigest()  


# 2. Use hashlib

import hashlib   

m2 = hashlib.md5()   
m2.update(sign_str)
print m2.hexdigest()  
