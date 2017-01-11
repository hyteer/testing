import requests
import json
import pytest


class Product(object):

    def product_list(self,conf):
        print "--- API: product_list ---"
        url = conf.URL+"/product/list-ajax"
        cookie = conf.get_cookie()
        r = requests.post(url,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        print "content:",content
        assert errcode == 0
        print "errcode is:%s" % errcode
        return content



