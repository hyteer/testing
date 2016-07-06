import requests
import json

data = {'fromapp': 'android', 'phone': '13828821487', 'password': '2580123456'}

r = requests.post("http://huimaidev.vikduo.com/appapi/user/login", data=data)


print "Response:",r.content
js = json.loads(r.text)
print "msg:",js['msg']
print "type:",js['type']
print "username:",js['data']['username']
print "usersession:",js['data']['usersession']



