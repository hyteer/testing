# coding: utf-8
"""
会员测试
"""
import requests
import json
import pytest


class TestClass:

    def test_member_list(self,conf):
        mb = conf.member
        r = mb.member_list(conf)
        print "resp:", r

    def test_member_detail(self,conf):
        mb = conf.member
        r = mb.member_detail(conf,conf.USER_ID)
        print "resp:", r

    def test_members_list(self,conf):
        mb = conf.member
        r = mb.members_list(conf)
        print "resp:", r

    def test_members_detail(self,conf):
        mb = conf.member
        r = mb.members_detail(conf,conf.MEMBER_ID)
        print "resp:", r

    def test_member_group_list(self,conf):
        mb = conf.member
        r = mb.member_group_list(conf)
        print "resp:", r




