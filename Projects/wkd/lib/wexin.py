# coding: utf-8
'''
微信前端配置和常用操作
'''
import sys


class Weixin(object):

    def user_center(self,str):
        '''
        进入个人中心页面
        :param str:
        :return:
        '''
        pass


class Menu(object):
    '''
    微信菜单配置
    '''
    BOTTOM = {
        'home': '''//li[@ng-click="switchTab('../mall/index')"]''',
        'goods': '''//li[@ng-click="switchTab('../product/category')"]''',
        'cart': '''//li[@ng-click="switchTab(col3.href)"]''',
        'suprise': '''//li[@ng-click="switchTab(col4.href)"]''',
        'user': '''//li[@ng-click="switchTab('../user/home')"]''',
    }


