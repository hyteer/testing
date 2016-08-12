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

        print u"---Test 获取商品列表---"
        url = self.baseurl+"/product/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_order_list(self,sessionid):

        print u"---Test 获取订单列表---"
        url = self.baseurl+"/order/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_order_detail(self,sessionid):
        """
        获取订单详情
        :param sessionid:
        :return: response content
        """
        print u"---Test 获取订单详情---"
        url = self.baseurl+"/order/get-order-detail-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        postdata = {'id': 989037}

        r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        print "Response:",r
        return r

    def get_product_detail(self,sessionid):
        """
        获取商品详情
        :param sessionid:
        :return: response content
        """
        print u"---Test 获取商品详情---"
        url = self.baseurl+"/product/get-detail-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        postdata = {'id': 285471}

        r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        print "Response:",r
        return r
    '''
    ########## 订单相关 ##########
    def order_add_ajax(self,sessionid):
        """
        创建普通订单
        :param sessionid:
        :return: response content
        """
        print u"---Test 创建普通订单---"
        url = self.baseurl+"/order/order-add-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        #product_info = [{'id': 286352'},{sku_id': ,'num': 1}]

        #postdata = {'products': product_info}

        r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        print "Response:",r
        return r
    '''

    ########## WeiXin相关 ##########

    def page_list_ajax(self,sessionid):

        print u"---Test 获取微信页面列表---"
        url = self.baseurl+"/page/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def page_edit_ajax(self,sessionid):
        """
        获取微信页面设置信息
        :param sessionid:
        :return: response content
        """
        print u"---Test 编辑页面---"
        url = self.baseurl+"/page/edit-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        postdata = {'id': 302}

        r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        print "Response:",r
        return r




