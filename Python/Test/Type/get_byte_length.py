# encoding:utf-8

str = "testing str"
cnstr = u"测试字符串长度"

scsp_str = u"Host: 10.100.100.82:16180\
Connection: keep-alive\
Accept-Encoding: gzip, deflate\
Accept: */*\
User-Agent: python-requests/2.12.0\
Content-Length: 1"

byt = bytes(str)

def utf8len(s):
    return len(s.encode('utf-8'))

print len(scsp_str)

print utf8len(str)
print utf8len(cnstr)
