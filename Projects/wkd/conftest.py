# coding: utf-8
import pytest

import lib.init as init
from lib.api.member import Member
from lib.common import Common
from lib.config import Config
from lib.config import get_config
from lib.param.utils import Utils


def pytest_addoption(parser):
    '''
    获取环境变量
    :param parser:
    '''

    parser.addoption("--testenv", action="store", default="auto",help="please input a testenv,eg.'test','dev','ci'")
    parser.addoption("--mydebug", action="store", default="no",help="input '--mydebug=yes' to print debug info.")


@pytest.fixture()
def init_conf(request):
    '''
    初始化
    :param request:
    '''
    print "\nInitializing environment..."
    env = request.config.getoption('--testenv')
    debug = request.config.getoption('--mydebug')
    cfg = get_config(env)
    Config.set_flag(1)
    Config.ENV = env
    print "Env:%s" % env
    if debug == 'yes':
        Config.DEBUG = 'yes'
    return cfg

@pytest.fixture()
def init_api_set(request):
    '''
    初始化API模块
    :param request:
    '''
    print "\nAPI logining..."
    env = request.config.getoption('--testenv')
    cfg = get_config(env)
    init.api_login(cfg)
    print "Initializing api sets..."
    Config.member = Member()
    Config.COMMON = Common()

@pytest.fixture(scope="module")
def conf(request):
    '''
    全局功能及配置
    :param request:
    '''
    flag = Config.get_flag()
    env = request.config.getoption('--testenv')
    cfg = get_config(env)
    if flag == 1:
        return cfg
    else:
        cfg = init_conf(request)
        init_api_set(request)
        return cfg

# 常用功能
@pytest.fixture
def u8filter():
    utils = Utils()
    return utils.utf8_filter

@pytest.fixture
def utils():
    Config.UTILS = Utils()

@pytest.fixture(scope="module")
def load_api():
    '''
    动态加载API模块
    :return:
    '''
    return Config.load_api_mod

@pytest.fixture(scope="module")
def load_mod():
    '''
    动态加载模块

    注：此方法可代替load_api()
    '''
    return Config.load_module





