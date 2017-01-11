# coding: utf-8
"""
API测试
"""
import json,time,datetime
import pytest


class TestClass:

    conf = None
    pd = None
    mb = None


    @pytest.fixture
    def setup(self,conf,load_api):
        assert load_api('product','member') is True
        pd = conf.LOADED_API['product']
        mb = conf.LOADED_API['member']

        self.pd = pd
        self.mb = mb
        self.conf = conf
        return conf

    @pytest.fixture
    def setup2(self,conf,load_mod):
        assert load_mod('product','member') is True
        pd = conf.LOADED_MODULES['product']
        mb = conf.LOADED_MODULES['member']

        self.pd = pd
        self.mb = mb
        self.conf = conf
        return conf

    # Tests
    def test_product_list(self,setup2):
        conf,mb = self.conf,self.mb
        r = mb.member_list(conf)
        print "resp:", r
        time.sleep(3)

    def test_member_list(self,setup):
        conf = self.conf
        mb = self.mb
        r = mb.member_list(conf)
        print "resp:", r
        print "last test."
        time.sleep(3)

    def test_card_coupons_list(self,conf,load_api):
        assert load_api('market') is True
        mk = conf.LOADED_API['market']
        r = mk.card_coupons_list(conf)
        print "resp:", r















