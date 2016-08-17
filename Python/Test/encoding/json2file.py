# encoding=utf8

import json,os

data = {"summary" : u"This is a unicode character: ☆测试"}
strpath = os.path.abspath(os.path.join('D:\\Temp\\', os.pardir, 'Python'))


print data

decoded_data = unicode(data)
print decoded_data

with open('decoded_data.json', 'w') as outfile:
    json.dump(decoded_data, outfile)