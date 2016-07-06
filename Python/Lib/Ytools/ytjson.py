# encoding: utf-8
import json

class JsonUtils(object):

    def __init__(self):
       pass

    def tojson(self,jsonstr):        #Def Keywords here...
        jsobj = json.loads(jsonstr)
        return jsobj

    def json_Test(self,jsonstr,arg1='nemo'):
        js = json.loads(jsonstr)
        print "Get a json string:" ,jsonstr
        #print "Json Object:",js
        print "Phone is:" ,js['phone']
        pass

    def print_json(self,jsonstr):
        print "Json content:",jsonstr

    def json_maisha(self,jsonstr):
        js = json.loads(jsonstr)
        ### not implement yet
        print "not implement yet"

