import requests

url = "http://betanewwsh.snsshop.net"
logurl = url+"/login/index"
s = requests.Session()

s.get(url)
r = s.get(logurl)

print(r.text)