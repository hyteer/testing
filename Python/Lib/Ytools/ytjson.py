# encoding: utf-8
import json

class JsonUtils(object):

    def __init__(self):
       pass

    def yt_tojson(self,jsonstr):        #Def Keywords here...
        jsobj = json.loads(jsonstr)
        return jsobj

    def yt_json_Test(self,jsonstr,arg1='nemo'):
        js = json.loads(jsonstr)
        print "Get a json string:" ,jsonstr
        #print "Json Object:",js
        print "Phone is:" ,js['phone']
        pass


