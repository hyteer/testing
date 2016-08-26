# encoding: utf-8
import requests
import json
import Cookie,os
from urllib import urlencode
from utils import CommonUtils
import settings as set


s = requests.Session()
s.get('http://weishanghuzhushou.betanewwx.snsshop.net/weishanghuzhushou/oauth/testing?id=13723226')

print u"---Test 创建普通订单---"
url = "http://weishanghuzhushou.betanewwx.snsshop.net/order/order-add-ajax"
headers = set.Wsh.headers

postdata = {'products[0][id]': 286603,'products[0][sku_id]':1167425,'products[0][num]':1,'pickup_type':1}

r = s.post(url, data=postdata,headers=headers)

print "Headers:", r.headers
print "Response:", r.content
print "Response:",r


