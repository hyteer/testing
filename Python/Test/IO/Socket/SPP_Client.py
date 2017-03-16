# coding: utf-8
# Socket client program for SCSP SPP
import socket
import sys

HOST = '10.100.100.88'    # The remote host
PORT = 13480              # The same port as used by the server
s = None
MSG = "ver=1&cmd=4010&src=1&biz_content=<xml><body><![CDATA[测试商户1]]></body><cashierid><![CDATA[]]></cashierid><mch_id>1000000013</mch_id><nonce_str><![CDATA[7vwzjzr0l9emxkdhw0mqw7u16rq55ygq]]></nonce_str><notify_url><![CDATA[http://betapay.speedpos.snsshop.net/notify/1000000013/P1000000013201703151145461111]]></notify_url><openid><![CDATA[oRs4Ywk9D3mNHfjVI22dfVanN-sA]]></openid><out_trade_no><![CDATA[P1000000013201703151145461111]]></out_trade_no><return_url><![CDATA[http://betapay.speedpos.snsshop.net/success/1000000013/P1000000013201703151145461111]]></return_url><sign><![CDATA[0C81D6022D4EDA3CDA630AFF05573FC3]]></sign><spbill_create_ip><![CDATA[10.20.100.200]]></spbill_create_ip><total_fee>1</total_fee><trade_type><![CDATA[WXPAY.JSAPI]]></trade_type></xml>\r\n"
MSG1 = 'Test from py..\r\n'

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
s.sendall(MSG)
data = s.recv(1024)
print("data:%s" % data)
s.close()
print 'Received', repr(data)