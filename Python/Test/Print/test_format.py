# encoding:utf-8

PD_NAME = 'YT'
SALES = 1288


PRODUCT_DATA = u'{"productInfo":{"detail_pic":"504987,504986,","detail":"<p>Auto:测试商品描述。。。</p>"},\
    "product":{"product_type":1,"name":"%s","sales":"%s","covers_id":504987,"quota":"{限额}",\
    "sort":"0","sale_scope":"1","product_category_id":36717,"product_category_path":"/36717/","status":2,\
    "postage_fee_type":0,"product_kind_ids":"243720;","show_sale_num":2,"prod_weight":"200"},\
    "shareMessage":{"desc":"优惠多多,欢迎选购","title":"${产品名称}","file_cdn_path":\
    "http://imgcache.vikduo.com/static/f5dd9217f985e4796717e33e41aabc1d.png","pic_id":504987},"kindBody":\
    [{"firstName":"100g","firstRowSpan":1,"firstShow":true,"id":"100g","status":false},{"firstName":"200g",\
    "firstRowSpan":1,"firstShow":true,"id":"200g","status":false}],"skus":[{"status":1,"reserves":${库存},\
    "market_price":"99","retail_price":"${价格}","sku_no":"T00001","barcode":"${条形码1}","sales":0,"name":\
    "${产品名称}","kind_value_ids":[944670],"kind_ids":[243720]},{"status":1,"reserves":${库存},"market_price":\
    "198","retail_price":"${价格}","sku_no":"T00002","barcode":"${条形码2}","sales":0,"name":"${产品名称}",\
    "kind_value_ids":[944671],"kind_ids":[243720]}]}' % (PD_NAME,SALES)


PD_DATA = '{"productInfo":{"detail_pic":"504987,504986,","detail":"<p>Auto:测试商品描述。。。</p>","name":"%s"}' % PD_NAME

print PRODUCT_DATA
print 'This is {name},(s)he is {age} old'.format(name='YT',age=33)




