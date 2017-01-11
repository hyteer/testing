# coding: utf-8
'''
API参数化配置
'''
from utils import Utils


class ApiParam(object):

    @staticmethod
    def card_coupons_add(title='default'):
        if title == 'default':
            title = "测试卡" + Utils.rand_str()
        data = {"brand_name":"微客联盟","title":title,"logo_url":"http://imgcache.vikduo.com/static/44ae6a2fae8d1ae7acddc0129dabb128.png","color":"#55bd47","date_info_type":1,"begin":1483977600,"end":1581436799,"quantity":"999","get_limit":"200","can_give_friend":1,"code_type":"3","notice":"请出示卡券二维码","description":"使用说明。。。","service_phone":"13344556677","card_type":1,"assign":-1,"wx_card_type":2,"card_money":0,"money_limit":0,"card_discount":"8.8","exchange_content_text":"","product_ids":"","deal_detail":"8.8折折扣券1张，全场通用"}
        return data

    @staticmethod
    def reduction_add(name='default'):
        if name == 'default':
            name = "满减" + Utils.rand_str()
        data = {"name":name,"is_relate_all":1,"start_time":1484115936,"end_time":1579587938,"conditions":[{"condition_type":1,"level":1,"condition_min":90000,"strategys":[{"reduction_type":1,"amount":20000,"discount":"","point":"","card_type_id":"","red_packet_id":"","is_all_area":1,"area_id":"","area_cn":"","is_limit":2},{"reduction_type":3,"amount":"","discount":"","point":"20","card_type_id":"","red_packet_id":"","is_all_area":1,"area_id":"","area_cn":"","is_limit":2}]}],"products":[]}
        return data

