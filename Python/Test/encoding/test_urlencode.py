#coding:utf8
import urllib

str = 'activity_name=JustaTest1&template=1&buy_limit=1&start_time=${start_time}&end_time=${end_time}&is_subscribe=2&share_award=2&use_points=2&points_num=0&limit_type=1&try_limit=5&winning_limit=2&activity_desc=1. 抽奖对象：所有用户；\
2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）\
3. #积分可以兑换一次抽奖机会，限制#次；\
4. 中奖限制：每人限中奖一次；\
5. 本活动最终解释权归XX商家所有。&prize[0][level]=0&prize[0][type]=1&prize[0][name]=谢谢参与！&prize[0][type_id]=&prize[0][prize_pic]=&prize[0][documentLib][file_cdn_path]=&prize[0][num]=0&prize[0][probability]=30&prize[0][$$hashKey]=object:42&prize[1][level]=1&prize[1][type]=1&prize[1][name]=华为P9&prize[1][type_id]=&prize[1][prize_pic]=91751&prize[1][documentLib][file_cdn_path]=http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png&prize[1][num]=1&prize[1][probability]=10&prize[1][$$hashKey]=object:43&prize[1][invalidInfo]=&prize[2][level]=2&prize[2][type]=5&prize[2][name]=红包测试&prize[2][type_id]=583&prize[2][prize_pic]=91753&prize[2][documentLib][file_cdn_path]=http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png&prize[2][num]=10&prize[2][probability]=20&prize[2][$$hashKey]=object:44&prize[2][invalidInfo]=&prize[3][level]=3&prize[3][type]=3&prize[3][name]=10&prize[3][type_id]=&prize[3][prize_pic]=91752&prize[3][documentLib][file_cdn_path]=http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png&prize[3][num]=20&prize[3][probability]=40&prize[3][$$hashKey]=object:45&prize[3][invalidInfo]=&expiry_time=1477632103&share_type=1&startNews[title]=极速大转盘，幸运转转转~&startNews[description]=亲，点击进入活动主页，意外惊喜等着你！&startNews[document_id]=3&shareMessage[title]=玩大转盘，轻轻一转好礼不断！&shareMessage[desc]=玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~&shareMessage[pic_id]=9'
data = urllib.quote(str)


print "data:",data

