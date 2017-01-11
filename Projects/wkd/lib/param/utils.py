# coding: utf-8
'''
辅助功能函数
'''
import sys
import random,string


class Utils(object):

    def utf8_filter(self,str):
        '''
        UTF8终端打印编码过滤
        :param str:
        :return:
        '''
        if sys.stdout.encoding == 'cp936':
            #sys.stdout = UnicodeStreamFilter(sys.stdout)
            return str
        elif sys.stdout.encoding == 'UTF-8':
            return str.encode('utf-8')
        else:
            return str.encode('utf-8')

    def float_compare(self,x,y,flag="yes"):
        '''
        浮点数比较
        :param x:
        :param y:
        :param flag: 可选参数：'yes'/'no',默认为'yes',即为正向比较，'no'为反向比较
        :return:True
        '''
        print "x:%s,y:%s" % (x,y)
        if flag == "yes":
            assert float(x) == float(y)
            return True
        else:
            assert float(x) != float(y)
            return True

    def floa_not_equalst(self,x,y):
        '''
        浮点数反向比较，即不等于
        :param x:
        :param y:
        :return: True
        '''
        print "x:%s,y:%s" % (x,y)
        assert float(x) != float(y)
        return True

    @staticmethod
    def rand_num():
        randNameX = string.join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 10)).replace(" ","")
        return randNameX

    @staticmethod
    def rand_str():
        randstr = string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')
        return randstr
