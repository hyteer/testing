import requests

HEADERS = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'YT': 'for debug'
        }
HEADERS_JSON = {
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Requests':'1',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type':'application/json;charset=UTF-8',
    'YT': 'for debug'
}


url = "http://betanewwsh.snsshop.net"
logurl = url+"/login/login-ajax"
data = {'username':'20160912','password':'123456'}
data2 = '{"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"","agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"","createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}'

s = requests.Session()
s.get(url)
###
r = s.post(logurl,data=data,headers=HEADERS)
### member-list
url_member = url + "/member/list-ajax"
r2 = s.post(url=url_member,data=data2)

print("resp:",r.content)
print("headers:",r.headers)
print("resp2:",r2.content)





