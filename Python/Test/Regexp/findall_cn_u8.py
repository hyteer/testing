# coding: utf-8
import re
def findPart(regex, text, name):
    res=re.findall(regex, text)
    if res:
        print "There are %d %s parts:\n"% (len(res), name)
    for r in res:
        print "\t",r.encode("utf8")

text ="#who#helloworld#a中文x#"

usample=unicode(text,'utf8')
findPart(u"#[\w\u2E80-\u9FFF]+#", usample, "unicode chinese")

text2 = "测试账号：1000518"
usample2 = unicode(text2,'utf8')

match = re.match(u"\u6d4b\u8bd5\u8d26\u53f7", usample2)
res2 = re.findall(u"\u8d26\u53f7", usample2)
res3 = re.findall(u"(?<=\u8d26\u53f7\uff1a).*", usample2)
match2 = re.match(u"#[\w\u2E80-\u9FFF]+#", usample)

print match2
print res2,res3