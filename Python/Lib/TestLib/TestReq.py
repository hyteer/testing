#encoding:utf-8
from Lib.YTRequests import ReqLib
import requests

req = ReqLib()
url_back ='http://betanewwsh.snsshop.net'
url_weixin = 'http://wkdianshang.betanewwx.snsshop.net/wkdianshang'
baseurl = url_back
url = 'http://wkdianshang.betanewwx.snsshop.net/wkdianshang/oauth/testing?id=13764541'
url_home = 'http://wkdianshang.betanewwx.snsshop.net/wkdianshang/user/home'
url_product_list = baseurl + '/product/list-ajax'
url_login = url_back + '/login/login-ajax'
url_subshop = 'http://betashopadmin.snsshop.net'
url_sub_close = url_subshop + '/shop/main-sub-close-ajax'
url_terminal_list = url_subshop + '/terminal/list-ajax'
'''
res = req.create_session('yt')
res2 = req.create_session('wsh')

print res

r = req.get_request('wsh',url='http://betanewwsh.snsshop.net/login/index')
print r.status_code
'''
## Use with session
ss = req.create_session('wsh',url=url_back)
print ss.cookies
cookie = req.get_cookie('wsh','PHPSESSID')
print "cookie:%s" % cookie

#### Native way
#ss = req.simple_session(url=url)
#resp = ss.get(url=url_home)
#print ss.headers
#resp = req.get_request('wsh',url=url_home)
#resp = req.post_request('wsh',url=url_product_list,data={"_page":1,"_page_size":20,"category_id":"","sort":1,"order":0,"name":"","is_member_discount":""})

headers = {'Content-Type':'application/x-www-form-urlencoded'}
data = {'username':'20160912','password':'123456','captcha':111}
resp = req.post_request('wsh',url='/login/login-ajax', data=data, headers=headers)
#### 商铺信息
resp_shop = req.post_request('wsh', url='/shop/get-ajax')
print resp_shop.text

#### 分店
data = {"id":98185}
cookies = {'PHPSESSID':cookie}
ss_sub = req.create_session('sub',url=url_subshop,cookies=cookies)
#resp_close = req.post_request('sub',url=url_sub_close,data=data)

resp_list = req.post_request('sub',url='/terminal/list-ajax',data=None)

print resp.text
#print resp_close.text
print resp_list.text

content = req.load_json(resp.content)
#errmsg = data['errmsg']
print "errmsg:",content
#print "newdata:",newdata





