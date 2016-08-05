# encoding: utf-8

from Lib.ApiWsh import api
from Lib.ApiWsh.api import settings

set = settings.Maisha

############ Wsh ###########
cm = api.Common()
sp = api.Shop()
mk = api.Marketing()
pd = api.Product()

# get_cookie
sid = cm.wsh_get_cookie()

# Login 登录
resptext = cm.wsh_login(sid)
'''
# actlist   获取活动列表
sp.wsh_actlist(sid)

# shop_get  获取商家信息
sp.wsh_shop_get(sid)
##### Marketing ####
# get_group_actlist
mk.get_group_actlist(sid)
# get_reduction_actlist
mk.get_reduction_actlist(sid)
# get_secondkill_actlist
mk.get_secondkill_actlist(sid)

mk.get_collectzan_actlist(sid)
'''
####Product####
pd.get_product_list(sid)
pd.get_order_list(sid)
pd.page_list_ajax(sid)
pd.page_edit_ajax(sid)
#pd.get_order_detail(sid)
#pd.get_product_detail(sid)
