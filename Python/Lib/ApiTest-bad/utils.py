# encoding: utf-8
import requests
import json
from urllib import urlencode


class Utils(object):

    def __init__(self):
        pass

    def maisha_test(self):
        print "mytest"

    def _utf8_urlencode(self, data):
        if isinstance(data,unicode):
            return data.encode('utf-8')
        if not isinstance(data,dict):
            return data
        utf8_data={}
        for k, v in data.iteritems():
            utf8_data[k] = unicode(v).encode('utf-8')
            return urlencode(utf8_data)
