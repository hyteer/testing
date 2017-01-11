# coding: utf-8
import requests
import json


class Market(object):
    '''
    市场营销模块
    '''


    def together_buy_list(self,conf):
        '''
        拼团活动列表
        :param conf:
        :return:
        '''
        print "--- API: together_buy_list ---"
        url = conf.URL+"/together-buy/list-ajax"
        cookie = conf.get_cookie()
        r = requests.post(url, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def card_coupons_list(self,conf):
        '''
        获取卡券列表
        :param conf:
        '''
        print "--- API: card_coupons_list ---"
        url = conf.URL+"/card-coupons/list-ajax"
        cookie = conf.get_cookie()
        r = requests.post(url, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def card_coupons_add(self,conf,args):
        '''
        添加卡券
        :param conf:
        '''
        print "--- API: card_coupons_add ---"
        url = conf.URL+"/card-coupons/add-ajax"
        cookie = conf.get_cookie()
        r = requests.post(url, data=args, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def card_coupons_send(self,conf,args):
        '''
        派发卡券
        :param conf:
        '''
        print "--- API: card_coupons_send ---"
        url = conf.URL+"/card-coupons/send-ajax"
        cookie = conf.get_cookie()

        r = requests.post(url, data=args, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def card_coupons_del(self,conf,id):
        '''
        删除卡券
        :param conf:
        '''
        print "--- API: card_coupons_del ---"
        url = conf.URL+"/card-coupons/del-ajax"
        cookie = conf.get_cookie()
        data = {"id":id}
        data = json.dumps(data)
        r = requests.post(url, data=data, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def reduction_list(self,conf):
        '''
        满减活动列表
        :param conf:
        '''
        print "--- API: reduction_list ---"
        url = conf.URL+"/reduction/list-ajax"
        cookie = conf.get_cookie()
        r = requests.post(url, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def reduction_add(self,conf,args):
        '''
        添加满减活动
        :param conf:
        '''
        print "--- API: reduction_add ---"
        url = conf.URL+"/reduction/add-ajax"
        cookie = conf.get_cookie()
        r = requests.post(url, data=args, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def reduction_open(self,conf,id):
        '''
        开启满减活动
        :param conf:
        '''
        print "--- API: reduction_open ---"
        url = conf.URL+"/reduction/open-ajax"
        cookie = conf.get_cookie()
        data = {"id":id}
        args = json.dumps(data)
        r = requests.post(url, data=args, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def reduction_close(self,conf,id):
        '''
        关闭满减活动
        :param conf:
        '''
        print "--- API: reduction_close ---"
        url = conf.URL+"/reduction/close-ajax"
        cookie = conf.get_cookie()
        data = {"id":id}
        args = json.dumps(data)
        r = requests.post(url, data=args, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def reduction_del(self,conf,id):
        '''
        删除满减活动
        :param conf:
        '''
        print "--- API: reduction_del ---"
        url = conf.URL+"/reduction/delete-ajax"
        cookie = conf.get_cookie()
        data = {"id":id}
        args = json.dumps(data)
        r = requests.post(url, data=args, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content

    def cash_redpack_list(self,conf):
        '''
        现金红包列表
        :param conf:
        '''
        print "--- API: cash_redpack_list ---"
        url = conf.URL+"/cash-redpack/list-ajax"
        cookie = conf.get_cookie()
        data = {"_page_size":15,"_page":1}
        data = json.dumps(data)
        r = requests.post(url, data=data, headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content






