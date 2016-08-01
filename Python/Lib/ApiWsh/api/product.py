# encoding: utf-8
import requests
import json
import Cookie,os
import settings as set

ws = set.Wsh()


class Product(object):
    baseurl = ws.baseurl
    proxylist = {'http' : 'http://127.0.0.1:8888'}
    headers = ws.headers

    ######### 商品 ##########
    def get_product_list(self,sessionid):

        print u"---Test 获商品列表---"
        url = self.baseurl+"/product/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_product_detail(self,sessionid):

        print u"---Test 获取商品详情---"
        url = self.baseurl+"/product/get-detail-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        postdata = {'id': 285649}

        r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r





