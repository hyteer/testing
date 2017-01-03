# coding: utf-8
import pytest
import time

@pytest.mark.nondestructive
def test_nondestructive(selenium):
    selenium.get('http://testnewwsh.snsshop.net/login/index')
    assert selenium.title ==  u"商户后台管理系统1"
    time.sleep(2)



