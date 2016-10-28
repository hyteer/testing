#encoding:utf-8
from Lib.YTRequests import ReqLib
import requests,json
from settings import config

cfg = config()
req = ReqLib()
debug=0
headers = {'Content-Type':'application/x-www-form-urlencoded'}


#-----------------获取Session
ss = req.create_session('wsh',url=cfg.URL,debug=1)
print ss.cookies
cookie = req.get_cookie('wsh','PHPSESSID')
cookies = {'PHPSESSID':cookie}

print "cookies:%s" % cookies
data = {'username':cfg.USER,'password':cfg.PASSWORD,'captcha':111}
resp = req.post_request('wsh',url='/login/login-ajax', data=data, headers=headers,debug=debug)

#--------------- 登录微信端
def login_weixin(cookies,debug=0):
    print u"登录微信..."
    ss_wx = req.create_session('wx',url=cfg.URL_WEIXIN,cookies=cookies, debug=debug)
    req.post_request('wx',url='/oauth/testing?id='+cfg.USER_ID, debug=debug)
    return ss_wx

#--------------- 登录分店
def login_subshop(cookies):
    print u"登录分店..."
    ss_sub = req.create_session('sub',url=cfg.URL_TERMINAL,cookies=cookies,debug=debug)
    return ss_sub


#### Native way
#ss = req.simple_session(url=url)
#resp = ss.get(url=url_home)
#print ss.headers
#resp = req.get_request('wsh',url=url_home)
#resp = req.post_request('wsh',url=url_product_list,data={"_page":1,"_page_size":20,"category_id":"","sort":1,"order":0,"name":"","is_member_discount":""})

#--------------- 测试接口

#商铺信息

#resp_shop = req.post_request('wsh', url='/shop/get-ajax',debug=debug)

# 添加商品

auto_data = '{"productInfo":{"detail_pic":"504987,504986,","detail":"<p>Auto:测试商品描述。。。</p>"},"product":{"product_type":1,"name":"${产品名称}","sales":"${销量}","covers_id":504987,"quota":"${限额}","sort":"0","sale_scope":"1","product_category_id":36717,"product_category_path":"/36717/","status":2,"postage_fee_type":0,"product_kind_ids":"243720;","show_sale_num":2,"prod_weight":"200"},"shareMessage":{"desc":"优惠多多,欢迎选购","title":"${产品名称}","file_cdn_path":"http://imgcache.vikduo.com/static/f5dd9217f985e4796717e33e41aabc1d.png","pic_id":504987},"kindBody":[{"firstName":"100g","firstRowSpan":1,"firstShow":true,"id":"100g","status":false},{"firstName":"200g","firstRowSpan":1,"firstShow":true,"id":"200g","status":false}],"skus":[{"status":1,"reserves":${库存},"market_price":"99","retail_price":"${价格}","sku_no":"T00001","barcode":"${条形码1}","sales":0,"name":"${产品名称}","kind_value_ids":[944670],"kind_ids":[243720]},{"status":1,"reserves":${库存},"market_price":"198","retail_price":"${价格}","sku_no":"T00002","barcode":"${条形码2}","sales":0,"name":"${产品名称}","kind_value_ids":[944671],"kind_ids":[243720]}]}'
pd_data = cfg.PRODUCT_DATA.encode(encoding='utf-8')

print cfg.PRODUCT_DATA
pddata = '{"productInfo":{"detail_pic":"733566,1054457,","detail":"<p>测试商品CI的详情。。。</p>"},"product":{"product_type":1,"name":"${产品名称}","sales":"${销量}","covers_id":733566,"quota":"5","sort":"0","sale_scope":"1","product_category_id":65,"product_category_path":"/86/7/","status":2,"postage_fee_type":"5500","product_kind_ids":"208520;","show_sale_num":2,"prod_weight":"280"},"shareMessage":{"desc":"优惠多多,欢迎选购","title":"${产品名称}","file_cdn_path":"http://imgcache.vikduo.com/static/bc9eebfe94619d95b3b9a226f0c24506.jpg","pic_id":1054457},"kindBody":[{"firstName":"500ml","firstRowSpan":1,"firstShow":true,"id":"500ml","status":false},{"firstName":"180ml","firstRowSpan":1,"firstShow":true,"id":"180ml","status":false}],"skus":[{"status":1,"reserves":${库存},"market_price":"128","retail_price":"${价格}","sku_no":"T0010001","barcode":"${条形码1}","sales":0,"name":"${产品名称}","kind_value_ids":[971511],"kind_ids":[208520]},{"status":1,"reserves":200,"market_price":"88","retail_price":"${价格}","sku_no":"T0010001","barcode":"${条形码2}","sales":0,"name":"${产品名称}","kind_value_ids":[988075],"kind_ids":[208520]}]}'
r_add_pd = req.post_request('wsh',url='/product/add-ajax', data=pd_data, headers=cfg.HEADERS_JSON, debug=1 )
#print r_add_pd.text
print r_add_pd.content
dict = json.loads(r_add_pd.text)
product_id = dict['errmsg']['product']['id']
sku_id = dict['errmsg']['skus'][0]['id']
print "product_id:%s, sku_id:%s" % (product_id,sku_id)

# 商品上架
data_onsale = '{"ids":[%d]}' % product_id
r_onsale = req.post_request('wsh',url='/product/on-sale-ajax', data=data_onsale, headers=cfg.HEADERS_JSON,debug=1)
print r_onsale.text

# 商品详情


# 分店
data = '{"id":981851}'
login_subshop(cookies)
#ss_sub = req.create_session('sub',url=cfg.URL_TERMINAL,cookies=cookies,debug=1)
#resp_close = req.post_request('sub',url='/shop/main-sub-close-ajax',data=data,debug=1)
#resp_open = req.post_request('sub',url='/shop/main-sub-open-ajax',data=data,debug=1)
#print resp_close.text
resp_list = req.post_request('sub',url='/terminal/list-ajax',data=None,debug=1)
print resp_list.text

# 前端
#ss_wx = req.create_session('wx',url=cfg.URL_WEIXIN,cookies=cookies, debug=1)
#req.post_request('wx',url='/oauth/testing?id='+cfg.USER_ID, debug=1)
headers = cfg.HEADERS_JSON
login_weixin(cookies,debug=1)
data_list = '{"_page":1,"_page_size":20,"category_id":"","sort":1,"order":0,"name":"","is_member_discount":""}'
data_pd = '{"id":291453}'
data_order = {'products[0][id]':product_id,'products[0][sku_id]':sku_id,'products[0][num]':1,'pickup_type':1}

r_order = req.post_request('wx',url='/order/order-add-ajax',data=data_order,debug=1 )
dict_order = json.loads(r_order.text)
print r_order.text
print "order_id:",dict_order['errmsg']['order']['id']

r_list = req.post_request('wx', url='/product/list-ajax',data=data_list,debug=1)
print r_list.text

#r_pd_detail = req.post_request('wx',url='/product/get-detail-ajax',data=data_pd, headers=headers, debug=1)



#print resp_close.text


#content = req.json_loads(resp.content)
#errmsg = data['errmsg']
#print "errmsg:",content
#print "newdata:",newdata





