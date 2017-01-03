# encoding: utf-8
import random,string
import os

ROOT_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

def rand_num():
        randNameX = string.join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 10)).replace(" ","")
        return randNameX

def rand_str():
    randstr = string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')
    return randstr


class Maisha():
    baseurl = 'http://huimaidev.vikduo.com/appapi'
    phone = '13828821487'
    password = '2580123456'
    defaultapp = 'android'
    testapp = 'testandroid'

class Config(object):

    CAPTCHA = '1111'
    PROXY = {'http' : 'http://127.0.0.1:8888'}
    #USER = 20151228
    #PASSWORD = 123456
    URL = 'http://betanewwsh.snsshop.net'
    #baseurl = 'http://testnewwsh.snsshop.net/'
    #baseurl = 'http://testnewwsh.nexto2o.com/'
    INIT_FLAG = 0
    ENV = 'default'
    SSID = None
    #COOKIE = {'PHPSESSID': SSID}

    @staticmethod
    def get_flag():
        return Config.INIT_FLAG

    @staticmethod
    def set_flag(flag):
        Config.INIT_FLAG = flag

    @staticmethod
    def get_cookie():
        return {'PHPSESSID': Config.SSID}


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

    randstr = rand_str()
    PD_NAME = u'测试商品-%s' % randstr
    SALES = random.randint(200,2000)
    RESERVERS = random.randint(100,500)
    PRICE = random.randint(1,100)
    CODE1 = rand_num()
    CODE2 = rand_num()

    PRODUCT_DATA = u'{"productInfo":{"detail_pic":"733566,1054457,","detail":"<p>测试商品CI的详情。。。\
    </p>"},"product":{"product_type":1,"name":"%s","sales":"%s","covers_id":733566,\
    "quota":"5","sort":"0","sale_scope":"1","product_category_id":65,"product_category_path":"/86/7/",\
    "status":2,"postage_fee_type":"5500","product_kind_ids":"208520;","show_sale_num":2,"prod_weight":"280"},\
    "shareMessage":{"desc":"优惠多多,欢迎选购","title":"%s","file_cdn_path":\
    "http://imgcache.vikduo.com/static/bc9eebfe94619d95b3b9a226f0c24506.jpg","pic_id":1054457},"kindBody":\
    [{"firstName":"500ml","firstRowSpan":1,"firstShow":true,"id":"500ml","status":false},{"firstName":\
    "180ml","firstRowSpan":1,"firstShow":true,"id":"180ml","status":false}],"skus":[{"status":1,\
    "reserves":%s,"market_price":"128","retail_price":"%s","sku_no":"T0010001","barcode":\
    "%s","sales":0,"name":"%s","kind_value_ids":[971511],"kind_ids":[208520]},\
    {"status":1,"reserves":%s,"market_price":"88","retail_price":"%s","sku_no":"T0010001",\
    "barcode":"%s","sales":0,"name":"%s","kind_value_ids":[988075],\
    "kind_ids":[208520]}]}' % (PD_NAME,SALES,PD_NAME,RESERVERS,PRICE,CODE1,PD_NAME,RESERVERS,PRICE,CODE2,PD_NAME)


class TestConfig(Config):
    USERNAME = 20161210
    PASSWORD = 123456
    USER_ID = '13764761'
    MEMBER_ID = '371'
    URL = 'http://testnewwsh.snsshop.net'
    URL_TERMINAL = 'http://testshopadmin.snsshop.net'



class BetaConfig(Config):
    USERNAME = 20151228
    PASSWORD = 123456
    USER_ID = '13764779'
    MEMBER_ID = '267'
    URL = 'http://betanewwsh.snsshop.net'

class AutoConfig(Config):
    USERNAME = 20160912
    PASSWORD = 123456
    USER_ID = '13764552'
    MEMBER_ID = '291'
    URL = 'http://betanewwsh.snsshop.net'
    URL_TERMINAL = 'http://betashopadmin.snsshop.net/'
    URL_WEIXIN = 'http://wkdianshang.betanewwx.snsshop.net/wkdianshang'

    randstr = rand_str()
    PD_NAME = u'测试商品-%s' % randstr
    SALES = random.randint(200,2000)
    RESERVERS = random.randint(100,500)
    PRICE = random.randint(1,100)
    CODE1 = rand_num()
    CODE2 = rand_num()

    PRODUCT_DATA = u'{"productInfo":{"detail_pic":"504987,504986,","detail":"<p>Auto:测试商品描述。。。</p>"},\
    "product":{"product_type":1,"name":"%s","sales":"%s","covers_id":504987,"quota":"5",\
    "sort":"0","sale_scope":"1","product_category_id":36717,"product_category_path":"/36717/","status":2,\
    "postage_fee_type":0,"product_kind_ids":"243720;","show_sale_num":2,"prod_weight":"200"},\
    "shareMessage":{"desc":"优惠多多,欢迎选购","title":"%s","file_cdn_path":\
    "http://imgcache.vikduo.com/static/f5dd9217f985e4796717e33e41aabc1d.png","pic_id":504987},"kindBody":\
    [{"firstName":"100g","firstRowSpan":1,"firstShow":true,"id":"100g","status":false},{"firstName":"200g",\
    "firstRowSpan":1,"firstShow":true,"id":"200g","status":false}],"skus":[{"status":1,"reserves":%s,\
    "market_price":"99","retail_price":"%s","sku_no":"T00001","barcode":"%s","sales":0,"name":\
    "%s","kind_value_ids":[944670],"kind_ids":[243720]},{"status":1,"reserves":%s,"market_price":\
    "198","retail_price":"%s","sku_no":"T00002","barcode":"%s","sales":0,"name":"%s",\
    "kind_value_ids":[944671],"kind_ids":[243720]}]}' % (PD_NAME,SALES,PD_NAME,RESERVERS,PRICE,CODE1,PD_NAME,RESERVERS,PRICE,CODE2,PD_NAME)


#config = CiConfig
#cfg = Config()
test_cfg = TestConfig()


def get_config(env):
    if env == "test":
        return TestConfig()
    elif env == "beta":
        return BetaConfig()
    elif env == "auto":
        return AutoConfig()
    elif env == "dev":
        return DevConfig()
    elif env == "ci":
        return CiConfig()
    else:
        print("Please input a legal env string,eg. 'test','auto','dev','ci'.")
        return None



'''
config = {
    'Dev': DevConfig,
    'Test': TestConfig,
    'Beta': BetaConfig

    'default': BetaConfig
}
'''


