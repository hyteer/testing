# coding: utf-8
"""
商品测试
"""
import requests
import json
import pytest


class TestClass:

    conf = None
    pd = None

    @pytest.fixture
    def setup(self,conf,load_api):
        assert load_api('product','member') is True
        pd = conf.LOADED_API['product']
        mb = conf.LOADED_API['member']
        self.pd = pd
        self.mb = mb
        self.conf = conf
        return conf

    def test_product_list(self,setup):
        conf = self.conf
        pd = self.pd
        r = pd.product_list(conf)
        print "resp:", r








