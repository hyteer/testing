# coding:utf-8
import re

str = u"<retmsg>第三方订单号已存在!</retmsg>"

matchs = re.findall(r"(?<=<retmsg>).*(?=<\/retmsg>)",str)

print matchs[0]

