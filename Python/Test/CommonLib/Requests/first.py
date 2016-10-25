import requests

r = requests.get(url='http://betanewwsh.snsshop.net/')    # Basic
print(r.status_code)    # response
#r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #with params
print(r.url)
ckjar = r.cookies
print(ckjar)
ck = ckjar._cookies
beta = ck['betanewwsh.snsshop.net']
baseck = beta['/']
cookie = baseck['PHPSESSID']

print("ck:",ck)
print("beta-cookie:",beta)
print("base dir:",baseck)
print("cookie value:",cookie.value)
#print(r.text)   #print resp text


