# encoding: utf-8

from Lib.ApiWsh import api
from Lib.ApiWsh.api import settings

#set = settings.Maisha

############ Wsh ###########
init = api.InitSession()
#cm = api.Common()
sp = api.Shop()
mk = api.Marketing()
pd = api.Product()
mb = api.Member()
wx = api.Weixin()

#### get_cookie
#sid = cm.wsh_get_cookie()

wxck = init.wsh_weixin_cookie()
wxss = init.wsh_weixin_session()
ssid = init.wsh_get_cookie()
#wxcookies = cm.wsh_weixin_cookie()

#### Login 登录
#resptext = cm.wsh_login(ssid)
init.wsh_login(ssid)



#### Marketing ####
#mk.get_market_act_list(sid)
#mk.get_market_add_ajax2(sid)
wx.wx_redpack_list_ss(wxss)
wx.wx_redpack_list_ck(wxck)
sp.wsh_shop_get(ssid)
sp.wsh_terminal_list_ajax(ssid)

#mk.market_egg_add_ajax(sid)
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
#### Product ####
#pd.get_product_list(sid)
#pd.get_togetherbuy_detail(sid)
'''
pd.get_product_list(sid)
pd.get_order_list(sid)
pd.page_list_ajax(sid)
pd.page_edit_ajax(sid)
pd.get_order_detail(sid)
pd.get_product_detail(sid)

#### Members ####
mb.wsh_member_list(sid)
mb.wsh_members_get_all_tags(sid)
mb.wsh_member_detail_ajax(sid)
'''
"""
#pd.order_test(wxcookies)
pd.order_add_ajax(wxcookies)

mb.wsh_member_list(sid)
mb.wsh_members_get_all_tags(sid)
mb.wsh_member_detail_ajax(sid)

mb.wsh_member_point_list(sid)
mb.wsh_members_detail(sid,256)
mb.wsh_members_list_ajax(sid)
mb.wsh_members_get_tag(sid)
"""

