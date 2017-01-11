# coding: utf-8
"""
API测试
"""
import json,time,datetime
import pytest

class TestCardCoupons:

    mk = None
    clsdata = {}
    USER_ID = '13764907'

    @pytest.fixture
    def setup(self,conf):
        mk = conf.API['market']()
        self.mk = mk
        return conf

    # Tests

    def test_card_coupons_list(self,conf):
        mk = conf.API['market']()
        r = mk.card_coupons_list(conf)
        print "resp:", r

    def test_card_coupons_add(self,conf):
        data = conf.API_PARAM.card_coupons_add()
        args = json.dumps(data)
        print("args:",args)
        mk = conf.API['market']()
        r = mk.card_coupons_add(conf,args)
        print "resp:", r
        print "card_id:", r['errmsg']['id']
        self.clsdata['card_id'] = r['errmsg']['id']

    def test_card_coupons_send(self,conf):
        id = self.clsdata['card_id']
        data = {"user_type":1,"card_type_id":id,"to_user_ids":[self.USER_ID]}
        args = json.dumps(data)
        print("args:",args)
        mk = conf.API['market']()
        r = mk.card_coupons_send(conf,args)
        print "resp:", r

    def test_card_coupons_del(self,conf):
        mk = conf.API['market']()
        id = self.clsdata['card_id']
        r = mk.card_coupons_del(conf,id)
        print "resp:", r

class TestReduction:
    '''
    满减活动API测试
    '''

    mk = None
    clsdata = {}
    USER_ID = '13764907'

    # Tests

    def test_reduction_list(self,conf):
        mk = conf.API['market']()
        r = mk.reduction_list(conf)
        print "resp:", r

    def test_reduction_add(self,conf):
        data = conf.API_PARAM.reduction_add()
        args = json.dumps(data)
        print("args:",args)
        mk = conf.API['market']()
        r = mk.reduction_add(conf,args)
        print "resp:", r
        print "id:", r['errmsg']['id']
        self.clsdata['reduction_id'] = r['errmsg']['id']

    def test_reduction_open(self,conf):
        mk = conf.API['market']()
        id = self.clsdata['reduction_id']
        r = mk.reduction_open(conf,id)
        print "resp:", r
        #time.sleep(5)

    def test_reduction_close(self,conf):
        mk = conf.API['market']()
        id = self.clsdata['reduction_id']
        r = mk.reduction_close(conf,id)
        print "resp:", r
        #time.sleep(5)

    def test_reduction_del(self,conf):
        mk = conf.API['market']()
        id = self.clsdata['reduction_id']
        r = mk.reduction_del(conf,id)
        print "resp:", r


class TestCashRedpack:
    '''
    红包活动API测试
    '''

    # Tests

    def test_cash_redpack_list(self,conf):
        mk = conf.API['market']()
        r = mk.cash_redpack_list(conf)
        print "resp:", r















