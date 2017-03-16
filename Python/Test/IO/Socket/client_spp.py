# coding: utf-8

import random
str1 = random.randrange(1000,9999)

str2 = 'ver=1&cmd=4010&src=1&biz_content=<xml><body><![CDATA[测试商户1]]></body><cashierid><![CDATA[]]></cashierid><mch_id>1000000013</mch_id><nonce_str><![CDATA[7vwzjzr0l9emxkdhw0mqw7u16rq55ygq]]></nonce_str><notify_url><![CDATA[http://betapay.speedpos.snsshop.net/notify/1000000013/P1000000013201703151145461111]]></notify_url><openid><![CDATA[oRs4Ywk9D3mNHfjVI22dfVanN-sA]]></openid><out_trade_no><![CDATA[P1000000013201703151145461111]]></out_trade_no><return_url><![CDATA[http://betapay.speedpos.snsshop.net/success/1000000013/P1000000013201703151145461111]]></return_url><sign><![CDATA[0C81D6022D4EDA3CDA630AFF05573FC3]]></sign><spbill_create_ip><![CDATA[10.20.100.200]]></spbill_create_ip><total_fee>1</total_fee><trade_type><![CDATA[WXPAY.JSAPI]]></trade_type></xml>\n'

if __name__=="__main__":    
        import socket    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        sock.connect(('10.100.100.88', 13480))    
        import time    
        flag = str(str1) 
        #while True:   
        time.sleep(3)    
        print 'send to server with value: %s \n' % flag   
        sock.send(flag)    
        print sock.recv(1024)   
                  
        sock.close() 