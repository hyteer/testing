import json
s = '{"name":"YT","phone":13823114422}'
js = json.loads(s)

print "Name:%s,Phone:%d"%(js['name'],js['phone'])
print "Json Object:",js


