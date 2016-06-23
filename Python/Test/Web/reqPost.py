# encoding: utf-8
str = '\u9a8c\u8bc1\u7801\u53d1\u9001\u6210\u529f\uff0c\u8bf7\u6ce8\u610f\u67e5\u6536'
str1 = bytes(b'\x31\x32\x61\x62').decode('ascii')
str2 = bytes(b'\x31\x32\x61\x62').decode('ascii')

str3 = bytes(b'\u9a8c\u8bc1\u7801\u53d1\u9001\u6210\u529f\uff0c\u8bf7\u6ce8\u610f\u67e5\u6536').decode('utf8')
print ord(u'\u9a8c')
ustr = str.encode('utf8',str)
print str3
print ustr
