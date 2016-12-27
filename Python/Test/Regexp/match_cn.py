# coding: utf-8
import re

str = re.compile(u"测试账号：1000518")

find = str.findall(u"\u8d26\u53f7")
match = str.match(u"账号")
print match


