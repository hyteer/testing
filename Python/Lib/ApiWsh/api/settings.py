# encoding: utf-8

class Maisha():
    baseurl = 'http://huimaidev.vikduo.com/appapi'
    phone = '13828821487'
    password = '2580123456'
    defaultapp = 'android'
    testapp = 'testandroid'

class WshConfig:
    CAPTCHA = '1111'
    PROXY = {'http' : 'http://127.0.0.1:8888'}
    #USER = 20151228
    #PASSWORD = 123456
    URL = 'http://betanewwsh.snsshop.net'
    #baseurl = 'http://testnewwsh.snsshop.net/'
    #baseurl = 'http://testnewwsh.nexto2o.com/'

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

class DevConfig(WshConfig):
    USER = 7638800811
    PASSWORD = 518000
    URL = 'http://335.newwsh.snsshop.net'

class TestConfig(WshConfig):
    USER = 20160705
    PASSWORD = 123456
    URL = 'http://testnewwsh.snsshop.net'
    URL_TERMINAL = 'http://testshopadmin.snsshop.net'


class BetaConfig(WshConfig):
    USER = 20151228
    PASSWORD = 123456
    URL = 'http://betanewwsh.snsshop.net'

class AutoConfig(WshConfig):
    USER = 20160912
    PASSWORD = 123456
    URL = 'http://betanewwsh.snsshop.net'
    URL_TERMINAL = 'http://betashopadmin.snsshop.net/'
    URL_WEIXIN = 'http://wkdianshang.betanewwx.snsshop.net/wkdianshang'

config = AutoConfig

'''
config = {
    'Dev': DevConfig,
    'Test': TestConfig,
    'Beta': BetaConfig

    'default': BetaConfig
}
'''


