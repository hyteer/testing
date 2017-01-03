import requests
import json
import pytest


params = {"_page":1,"_page_size":20,"nickname":"","group_id":None,"shop_sub_id":"","agent_id":"","is_search":False,"belong_to_staff_id":"","createStart":"","createEnd":"","group_ids":[],"yestoday":False,"user_platform":0,"tags":[]}


class TestClass:

    baseurl = None
    headers = None

    def test_setup(self,conf):
        self.baseurl = conf.URL
        self.headers = conf.HEADERS
        print self.baseurl

    '''
    @pytest.fixture(scope='function')
    def setup_class(self,conf):
        self.baseurl = conf.URL
        self.headers = conf.HEADERS
        #return conf


    def test_conf(self,setup_class):
        import pdb
        pdb.set_trace()
        print("URL:%s" % setup_class.URL)
    '''

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_api_member_list(self,conf,fx_api_login):
        url = conf.URL+"/member/list-ajax"
        #cookie = fx_api_login(conf)
        postdata = '{"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"",' \
                   '"agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"",' \
                   '"createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}'
        #import pdb
        #pdb.set_trace()
        #print("baseurl:%s" % conf.URL)
        cookie = conf.get_cookie()
        r = requests.post(url, data=postdata,headers=conf.HEADERS_JSON,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print "errcode is:%s" % errcode
        print r.text
