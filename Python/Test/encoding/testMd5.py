def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

str = "body=test1&cashierid=1&mch_id=1000000037&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=oRs4YwmoyqGiWYqZn5FG0QCxlu9Q&out_trade_no=10002000711177073802461836cb&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=lg81oqo89knyugdifr850molrioeqw46"
md5str = md5(str)

print "md5:",md5str