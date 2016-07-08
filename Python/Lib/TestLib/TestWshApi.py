# encoding: utf-8

from Lib.ApiWsh import api
from Lib.ApiWsh.api import settings

set = settings.Maisha

############ MaiSha ###########
cm = api.Common()
sp = api.Shop()


# get_cookie
sid = cm.wsh_get_cookie()

# Login 登录
resptext = cm.wsh_login(sid)

# actlist   获取活动列表
sp.wsh_actlist(sid)

# shop_get  获取商家信息
sp.wsh_shop_get(sid)
