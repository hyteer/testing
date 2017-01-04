# coding: utf-8
# content of tests/conftest.py

#import time
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
import pytest
from operations.common import login,float_compare
from config import Config
#cfg = Config()
from config import get_config
import operations.common as cm
from operations.api.member import Member
import operations.tools as tools

mb = Member()
#INIT_FLAG = False
#env = None


# 获取环境变量
def pytest_addoption(parser):

    #parser.addoption("--hostname", action="store", default='127.0.0.1', help="specify IP of test host")
    parser.addoption("--testenv", action="store", default="test",help="please input a testenv,eg.'test','beta','ci'")
    parser.addoption("--mydebug", action="store", default="no",help="input '--mydebug=yes' to print debug info.")
    #import pdb
    #pdb.set_trace()
    #print "test addoption..."


@pytest.fixture(scope='module')
def db(request):
    return 'CONNECTED TO [' + request.config.getoption('--hostname') + '] SUCCESSFULLY!'
'''
@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption('--testenv')
'''
@pytest.fixture()
def init_conf(request):
    print "\nInitializing environment..."
    env = request.config.getoption('--testenv')
    debug = request.config.getoption('--mydebug')
    #import pdb
    #pdb.set_trace()
    cfg = get_config(env)
    Config.set_flag(1)
    Config.ENV = env
    print "Env:%s" % env
    if debug == 'yes':
        Config.DEBUG = 'yes'
    #cm.api_login(cfg)
    return cfg



@pytest.fixture()
def init_api_set(request):
    print "\nAPI logining..."
    env = request.config.getoption('--testenv')
    cfg = get_config(env)
    cm.api_login(cfg)
    print "Initializing api sets..."
    Config.member = Member()

# 全局功能及配置

@pytest.fixture()
def conf(request):
    flag = Config.get_flag()
    env = request.config.getoption('--testenv')
    cfg = get_config(env)
    if flag == 1:
        import pdb
        #pdb.set_trace()
        return cfg
    else:
        #import pdb
        #pdb.set_trace()
        cfg = init_conf(request)
        init_api_set(request)
        return cfg

@pytest.fixture
def username():
    return '20161210'

@pytest.fixture
def wsh_login():
    return login

@pytest.fixture
def float_comp():
    return float_compare

@pytest.fixture
def fx_api_login():
    #from operations.common import api_login
    return cm.api_login

@pytest.fixture
def u8filter():
    return tools.utf8_filter


