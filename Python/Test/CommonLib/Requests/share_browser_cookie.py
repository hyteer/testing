from selenium import webdriver
import time
import requests

url = "http://betanewwsh.snsshop.net/"

b = webdriver.Chrome()
#b = webdriver.Ie()
b.delete_all_cookies()
cookies = {}
while True:
    list_cookies = b.get_cookies()  #return a dict
    print(list_cookies)
    for s in list_cookies:
        cookies[s['name']] = s['value']
    print(cookies)
    if cookies.has_key('PHPSESSID'):
        b.close()
        break
    time.sleep(2)

#sn = requests.Session()
#requests.utils.add_dict_to_cookiejar(sn.cookies, cookies)
requests.get(url, cookies=cookies)
