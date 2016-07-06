# encoding: utf-8
import requests
import json
from urllib import urlencode

class ApiTest(object):

    def __init__(self):
       pass

    def _utf8_urlencode(self, data):
        if isinstance(data,unicode):
            return data.encode('utf-8')
        if not isinstance(data,dict):
            return data
        utf8_data={}
        for k, v in data.iteritems():
            utf8_data[k] = unicode(v).encode('utf-8')
            return urlencode(utf8_data)

    def api_userlogin(self,data='default',debug=0):
        file = open("d:/Res/MaishaReq.txt","r")
        content = file.read()
        if debug == 1:
            print "file content is:",content
        if data == 'default':
            postdata = {'fromapp': 'android', 'phone': '13828821487', 'password': '2580123456'}
        else:
            postdata = data
        r = requests.post("http://huimaidev.vikduo.com/appapi/user/login", data=postdata)
        print "Response:",r.content
        js = json.loads(r.text)
        print "msg:",js['msg']
        print "type:",js['type']
        print "username:",js['data']['username']
        print "usersession:",js['data']['usersession']

