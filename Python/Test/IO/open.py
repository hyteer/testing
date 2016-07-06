import re
import json

"""
MaishaReq.txt:
{
	"fromapp": "android",
	"phone": "13828821487",
	"password": "2580123456"
}
"""

file = open("d:/Res/MaishaReq2.txt","r")
content = file.read()
print content

# JSON test
js = json.loads(content)
print "json:",js
print "phone:",js['phone']

