# encoding: utf-8
import requests
import json

class ApiTest(object):

    def __init__(self):
       pass

    def yt_api_userlogin(self,data='default',debug=0):
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

    def yt_api_upload_file(self):
        files = {'upload_file': open('file.txt','rb')}
        values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
        url = "http://huimaidev.vikduo.com/appapi/common/upload_file"
        r = requests.post(url, files=files, data=values)

