# coding: utf-8
import json

dict = {"try_limit": "5\r", "prize[1][documentLib][file_cdn_path]": "http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png\r", "prize[0][type]": "1\r", "marketing_manage_id": "0\r", "prize[3][name]": "10\r", "prize[2][level]": "2\r", "prize[1][type_id]": "\r", "is_collect": "2\r", "prize[1][probability]": "1\r", "prize[2][documentLib][file_cdn_path]": "http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png\r", "prize[2][type]": "5\r", "prize[3][num]": "100\r", "prize[3][$$hashKey]": "object:57\r", "shareMessage[pic_id]": "36790\r", "buy_limit": "1\r", "collection_info_setting": "\r", "prize[3][prize_pic]": "91752\r", "prize[0][$$hashKey]": "object:54\r", "prize[0][probability]": "19\r", "expiry_time": "1579756342\r", "prize[1][invalidInfo]": "\r", "prize[0][type_id]": "\r", "prize[1][level]": "1\r", "prize[0][documentLib][file_cdn_path]": "\r", "prize[0][prize_pic]": "\r", "template": "4\r", "prize[0][name]": "\u8c22\u8c22\u53c2\u4e0e\uff01\r", "prize[1][type]": "1\r", "prize[3][type_id]": "\r", "use_points": "2\r", "prize[2][probability]": "30\r", "prize[1][$$hashKey]": "object:55\r", "prize[2][prize_pic]": "91753\r", "prize[0][num]": "0\r", "prize[3][probability]": "50\r", "start_time": "1484197822\r", "share_award": "2\r", "prize[3][type]": "3\r", "share_type": "1\r", "prize[0][level]": "0\r", "prize[2][num]": "50\r", "prize[1][num]": "3\r", "prize[3][invalidInfo]": "\r", "prize[2][$$hashKey]": "object:56\r", "prize[2][type_id]": "405\r", "prize[2][invalidInfo]": "\r", "points_num": "0\r", "prize[3][level]": "3\r", "activity_desc": "砸金蛋活动规则说明：\n1.活动时间：××××年××月××日-××××年××月××日；\n2.抽奖对象：所有用户/购买过商品的用户；\n3.用户必须关注微信公众号才能参与活动；（打开“强制关注”后）\n4.用户必须填写用户信息后才能参加活动；（打开“填写用户信息规则”后）\b5.分享并成功邀请好友赠送一次机会，同一个好友只有一次；\n6.次数限制：每天限制#次/总共可参加#次；\n7.积分抽奖：#积分可换取一次抽奖机会，最多可换取#次；\n8.中奖次数：每人限中奖一次；\n9.本活动最终解释权归XX商家所有。\r", "winning_limit": "2\r", "startNews[document_id]": "36791\r", "prize[2][name]": "\u6d4b\u8bd5\u7ea2\u5305\r", "prize[1][prize_pic]": "91751\r", "prize[3][documentLib][file_cdn_path]": "http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png\r", "prize[1][name]": "\u534e\u4e3aMate9\r", "is_subscribe": "2\r", "limit_type": "1\r", "startNews[description]": "\u4eb2\uff0c\u70b9\u51fb\u8fdb\u5165\u6d3b\u52a8\u4e3b\u9875\uff0c\u610f\u5916\u60ca\u559c\u7b49\u7740\u4f60\uff01\r", "end_time": "1578805824\r", "shareMessage[desc]": "\u73a9\u62bd\u5956\u7838\u91d1\u86cb\uff0c\u5343\u4e07\u5956\u54c1\u7b49\u4f60\u6765\uff0c\u767e\u5206\u767e\u8d62\u4e2d\u5956\u54df~\r", "activity_name": "\u7838\u91d1\u86cb\u6d4b\u8bd5\r", "startNews[title]": "\u4e00\u9524\u5b9a\u97f3\uff0c\u5f00\u5fc3\u7838\u91d1\u86cb~\r", "shareMessage[title]": "\u8f7b\u8f7b\u4e00\u9524\uff0c\u7838\u51fa\u7cbe\u5f69\uff01\r"}

print dict['try_limit']

def handle():
    for key in dict.keys():
        print key
        if key == "":
            dict['activity_desc'] += ("\n" + dict[key])

def show():
    for key in dict.keys():
        print "%s: %s" % (key,dict[key])

#print dict['activity_desc']

show()
jsonstr = json.dumps(dict)
print jsonstr
