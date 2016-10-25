# encoding: utf-8
import requests
import random
import string,urllib
import json
import Cookie,os
#import settings as set
from settings import config

cfg = config()

#ws = set.Wsh()


class Marketing(object):
    capt = cfg.CAPTCHA
    user = cfg.USER
    passwd = cfg.PASSWORD
    baseurl = cfg.URL
    proxylist = cfg.PROXY
    headers = cfg.HEADERS
    headers_json = cfg.HEADERS_JSON

    ######### 销售活动 ##########
    def get_group_actlist(self,sessionid):

        print u"---Test 获取拼团活动列表---"
        url = self.baseurl+"/together-buy/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_reduction_actlist(self,sessionid):

        print u"---Test 获取满减活动列表---"
        url = self.baseurl+"/reduction/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_secondkill_actlist(self,sessionid):

        print u"---Test 获取秒杀活动列表---"
        url = self.baseurl+"/second-kill/list-ajax"
        #url = "http://betanewwsh.vikduo.com/reduction/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    ######### 推广活动 ##########
    def get_collectzan_actlist(self,sessionid):

        print u"---Test 获取众筹活动列表---"
        url = self.baseurl+"/collect-zan/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_market_act_list(self,sessionid):

        print u"---Test 获取大转盘活动列表---"
        url = self.baseurl+"/market-activity/list-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        r = requests.post(url, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_market_add_ajax(self,sessionid):

        print u"---Test 添加大转盘活动列表---"
        ranstr = string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')
        act_name = 'P大转盘活动'+ranstr
        url = self.baseurl+"/market-activity/add-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        postdata = {
            'activity_name':act_name,
            'template':1,
            'buy_limit':1,
            'start_time':1475963849,
            'end_time':1476193054,
            'is_subscribe':2,
            'share_award':2,
            'use_points':2,
            'points_num':0,
            'limit_type':1,
            'try_limit':5,
            'winning_limit':2,
            'activity_desc':'1. 抽奖对象：所有用户；\
                            \n2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）\
                            \n3. #积分可以兑换一次抽奖机会，限制#次；\
                            \n4. 中奖限制：每人限中奖一次；\
                            \n5. 本活动最终解释权归XX商家所有。',
            'prize[0][level]':0,
            'prize[0][type]':1,
            'prize[0][name]':'谢谢参与！',
            'prize[0][num]':0,
            'prize[0][probability]':30,
            'prize[1][level]':1,
            'prize[1][type]':1,
            'prize[1][name]':'华为Watch',
            'prize[1][prize_pic]':91751,
            'prize[1][documentLib][file_cdn_path]':'http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png',
            'prize[1][num]':1,
            'prize[1][probability]':10,
            'prize[2][level]':2,
            'prize[2][type]':5,
            'prize[2][name]':'红包测试',
            'prize[2][type_id]':583,
            'prize[2][prize_pic]':91753,
            'prize[2][documentLib][file_cdn_path]':'http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png',
            'prize[2][num]':10,
            'prize[2][probability]':20,
            'prize[3][level]':3,
            'prize[3][type]':3,
            'prize[3][name]':10,
            'prize[3][prize_pic]':91752,
            'prize[3][documentLib][file_cdn_path]':'http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png',
            'prize[3][num]':20,
            'prize[3][probability]':40,
            'expiry_time':1477682103,
            'share_type':1,
            'startNews[title]':'极速大转盘，幸运转转转~',
            'startNews[description]':'亲，点击进入活动主页，意外惊喜等着你！',
            'startNews[document_id]':3,
            'shareMessage[title]':'玩大转盘，轻轻一转好礼不断！',
            'shareMessage[desc]':'玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~',
            'shareMessage[pic_id]':9
        }

        r = requests.post(url,data=postdata, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def market_egg_add_ajax(self,sessionid):

        print u"---Test 添加砸金蛋活动列表---"
        ranstr = string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')
        act_name = '砸金蛋活动'+ranstr
        url = self.baseurl+"/market-activity/add-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}
        postdata = {
            'activity_name':act_name,
            'template':4,
            'buy_limit':1,
            'start_time':1475953849,
            'end_time':1476163054,
            'is_subscribe':2,
            'share_award':2,
            'use_points':2,
            'points_num':0,
            'limit_type':1,
            'try_limit':8,
            'winning_limit':1,
            'activity_desc':'\n2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）'
                            '\n3. #积分可以兑换一次抽奖机会，限制#次；'
                            '\n1.抽奖对象：所有用户/购买过商品的用户；'
                            '\n2.用户必须关注微信公众号才能参与活动；（打开强制关注后）'
                            '\n3.分享并成功邀请好友赠送一次机会，同一个好友只有一次；'
                            '\n4.次数限制：每天限制#次/总共可参加#次；'
                            '\n5.积分抽奖：#积分可换取一次抽奖机会，最多可换取#次；'
                            '\n6.中奖次数：每人限中奖一次；'
                            '\n7.本活动最终解释权归XX商家所有。',
            'prize[0][level]':0,
            'prize[0][type]':1,
            'prize[0][name]':'谢谢参与！',
            'prize[0][num]':0,
            'prize[0][probability]':30,
            'prize[1][level]':1,
            'prize[1][type]':1,
            'prize[1][name]':'iPhone7',
            'prize[1][prize_pic]':91751,
            'prize[1][documentLib][file_cdn_path]':'http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png',
            'prize[1][num]':1,
            'prize[1][probability]':10,
            'prize[2][level]':2,
            'prize[2][type]':5,
            'prize[2][name]':'红包测试',
            'prize[2][type_id]':583,
            'prize[2][prize_pic]':91753,
            'prize[2][documentLib][file_cdn_path]':'http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png',
            'prize[2][num]':10,
            'prize[2][probability]':20,
            'prize[3][level]':3,
            'prize[3][type]':3,
            'prize[3][name]':10,
            'prize[3][prize_pic]':91752,
            'prize[3][documentLib][file_cdn_path]':'http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png',
            'prize[3][num]':20,
            'prize[3][probability]':40,
            'expiry_time':1477662103,
            'share_type':1,
            'startNews[title]':'一锤定音，开心砸金蛋~',
            'startNews[description]':'亲，点击进入活动主页，意外惊喜等着你！',
            'startNews[document_id]':36791,
            'shareMessage[title]':'轻轻一锤，砸出精彩！',
            'shareMessage[desc]':'玩抽奖砸金蛋，千万奖品等你来，百分百赢中奖哟~',
            'shareMessage[pic_id]':36790
        }

        r = requests.post(url,data=postdata, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

    def get_market_add_ajax2(self,sessionid):

        print u"---Test 添加大转盘活动2---"
        ranstr = string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')
        act_name = 'P大转盘活动'+ranstr
        url = self.baseurl+"/market-activity/add-ajax"
        headers = self.headers
        cookies = {'PHPSESSID': sessionid}

        str = 'activity_name=JustaTest1&template=1&buy_limit=1&start_time=${start_time}&end_time=${end_time}&is_subscribe=2&share_award=2&use_points=2&points_num=0&limit_type=1&try_limit=5&winning_limit=2&activity_desc=1. 抽奖对象：所有用户；\
            2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）\
            3. #积分可以兑换一次抽奖机会，限制#次；\
            4. 中奖限制：每人限中奖一次；\
            5. 本活动最终解释权归XX商家所有。&prize[0][level]=0&prize[0][type]=1&prize[0][name]=谢谢参与！&prize[0][type_id]=&prize[0][prize_pic]=&prize[0][documentLib][file_cdn_path]=&prize[0][num]=0&prize[0][probability]=30&prize[0][$$hashKey]=object:42&prize[1][level]=1&prize[1][type]=1&prize[1][name]=华为P9&prize[1][type_id]=&prize[1][prize_pic]=91751&prize[1][documentLib][file_cdn_path]=http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png&prize[1][num]=1&prize[1][probability]=10&prize[1][$$hashKey]=object:43&prize[1][invalidInfo]=&prize[2][level]=2&prize[2][type]=5&prize[2][name]=红包测试&prize[2][type_id]=583&prize[2][prize_pic]=91753&prize[2][documentLib][file_cdn_path]=http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png&prize[2][num]=10&prize[2][probability]=20&prize[2][$$hashKey]=object:44&prize[2][invalidInfo]=&prize[3][level]=3&prize[3][type]=3&prize[3][name]=10&prize[3][type_id]=&prize[3][prize_pic]=91752&prize[3][documentLib][file_cdn_path]=http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png&prize[3][num]=20&prize[3][probability]=40&prize[3][$$hashKey]=object:45&prize[3][invalidInfo]=&expiry_time=1477632103&share_type=1&startNews[title]=极速大转盘，幸运转转转~&startNews[description]=亲，点击进入活动主页，意外惊喜等着你！&startNews[document_id]=3&shareMessage[title]=玩大转盘，轻轻一转好礼不断！&shareMessage[desc]=玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~&shareMessage[pic_id]=9'
        postdata = urllib.quote(str)


        r = requests.post(url,data=postdata, headers=headers,cookies=cookies)
        print "Headers:", r.headers
        print "Response:", r.content
        return r

