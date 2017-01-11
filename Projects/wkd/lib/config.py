# encoding: utf-8

import os
from api.member import Member
from api.product import Product
from wexin import Weixin, Menu
from api.market import Market
from param.api import ApiParam


ROOT_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


class Config(object):
    '''
    基础配置
    '''

    CAPTCHA = '1111'
    PROXY = {'http' : 'http://127.0.0.1:8888'}
    URL = 'http://testwkd.snsshop.net/login/index'
    INIT_FLAG = 0
    ENV = 'default'
    SSID = None
    COOKIE = None
    DEBUG = 'no'
    API = {
        'member':Member,
        'product':Product,
        'market':Market
    }
    MODULES = {
        'member':Member,
        'product':Product,
        'weixin':Weixin
    }
    API_PARAM = ApiParam

    LOADED_API = {}
    LOADED_MODULES = {}
    WX_MENU = Menu


    @staticmethod
    def get_flag():
        return Config.INIT_FLAG

    @staticmethod
    def set_flag(flag):
        Config.INIT_FLAG = flag

    @staticmethod
    def get_cookie():
        return {'PHPSESSID': Config.SSID}

    @staticmethod
    def load_api_mod(*params):
        for mod in params:

            if mod in Config.API and mod not in Config.LOADED_API:
                api = Config.API[mod]
                Config.LOADED_API[mod] = api()

        return True

    @staticmethod
    def load_module(*params):
        for param in params:

            if param in Config.MODULES and param not in Config.LOADED_MODULES:
                module = Config.MODULES[param]
                Config.LOADED_MODULES[param] = module()

        return True




    HEADERS = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'YT': 'for debug'
        }
    HEADERS_JSON = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type':'application/json;charset=UTF-8',
        'YT': 'for debug'
    }


class AutoConfig(Config):
    '''
    微客多自动化测试环境配置(自动化测试专用)
    '''
    USERNAME = '20170108@qq.com'
    PASSWORD = '123456'
    USER_ID = '13764904'
    MEMBER_ID = '380'
    URL = 'http://testwkd.snsshop.net'
    URL_TERMINAL = 'http://testwkdshopadmin.snsshop.net'
    WX_URL = 'http://wkdianshang.testwkdwx.snsshop.net/wkdianshang'
    TITLE = u"微客多后台管理系统"

class TestConfig(Config):
    '''
    微客多测试环境配置(手工测试环境)
    '''
    USERNAME = 20160809
    PASSWORD = 123456
    USER_ID = '13764874'
    MEMBER_ID = '373'
    URL = 'http://testwkd.snsshop.net'
    URL_TERMINAL = 'http://testwkdshopadmin.snsshop.net'
    WX_URL = 'http://wkdianshang.testwkdwx.snsshop.net/wkdianshang'
    TITLE = u"微客多后台管理系统"

class BetaConfig(Config):
    USERNAME = 20151228
    PASSWORD = 123456
    USER_ID = '13764779'
    MEMBER_ID = '267'
    URL = 'http://betanewwsh.snsshop.net'
    TITLE = u"商户后台管理系统"


class DevConfig(Config):
    USER = 7638800811
    PASSWORD = 518000
    URL = 'http://335.newwsh.snsshop.net'

class CiConfig(Config):
    USER = 7638800811
    PASSWORD = 518000
    USER_ID = '137240011'
    URL = 'http://shanghutest.cxm'
    URL_TERMINAL = 'http://shopadmintest.cxm'
    URL_WEIXIN = 'http://scliveapp2015.weixintest.cxm/scliveapp2015'




def get_config(env):
    if env == "auto":
        return AutoConfig()
    elif env == "test":
        return TestConfig()
    elif env == "beta":
        return BetaConfig()
    elif env == "dev":
        return DevConfig()
    elif env == "ci":
        return CiConfig()
    else:
        print("Please input a legal env string,eg. 'test','wkd','auto','dev','ci'.")
        return None



