# encoding: utf-8
import os
from urllib import urlencode

class CommonUtils(object):

    def __init__(self):
       pass

    def printVersion(self):
        print u"【Ytools Library】 Version Number:1.0.1"

    def get_path(self,curdir,subdir):
        # Get a dir's path
        path = None
        if dir == None:
            path = curdir
        else:
            path = os.path.abspath(os.path.join(curdir, os.pardir, subdir))
        return path

    def _utf8_urlencode(self, data):
        if isinstance(data,unicode):
            return data.encode('utf-8')
        if not isinstance(data,dict):
            return data
        utf8_data={}
        for k, v in data.iteritems():
            utf8_data[k] = unicode(v).encode('utf-8')
            return urlencode(utf8_data)