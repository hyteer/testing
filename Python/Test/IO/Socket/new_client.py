# coding: utf-8

HOST = 'localhost'
PORT = 12345

HOST2 = '10.100.100.88'
PORT2 = 13480
MSG = "ver=1&cmd=4010&src=1&biz_content=<xml><body><![CDATA[测试商户1]]></body><cashierid><![CDATA[]]></cashierid><mch_id>1000000013</mch_id><nonce_str><![CDATA[7vwzjzr0l9emxkdhw0mqw7u16rq55ygq]]></nonce_str><notify_url><![CDATA[http://betapay.speedpos.snsshop.net/notify/1000000013/P1000000013201703151145461111]]></notify_url><openid><![CDATA[oRs4Ywk9D3mNHfjVI22dfVanN-sA]]></openid><out_trade_no><![CDATA[P1000000013201703151145461111]]></out_trade_no><return_url><![CDATA[http://betapay.speedpos.snsshop.net/success/1000000013/P1000000013201703151145461111]]></return_url><sign><![CDATA[0C81D6022D4EDA3CDA630AFF05573FC3]]></sign><spbill_create_ip><![CDATA[10.20.100.200]]></spbill_create_ip><total_fee>1</total_fee><trade_type><![CDATA[WXPAY.JSAPI]]></trade_type></xml>\r\n"

def socket_test(host,port,msg=None):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print "Connect sucess..."
    import time
    time.sleep(2)
    if msg == None:
        msg = 'test12\r\n'
    print "Msg:%s" % msg
    sock.send(msg)
    print sock.recv(1024)
    sock.close()



if __name__ == '__main__':
    socket_test(HOST2,PORT2,MSG)