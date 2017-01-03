import requests
import Cookie

def test_api_login(conf):

    cfg = conf('test')
    baseurl = cfg.URL
    headers = cfg.HEADERS
    captcha = cfg.CAPTCHA
    username = cfg.USERNAME
    password = cfg.PASSWORD

    r = requests.get(baseurl, headers=headers)
    cookies = r.headers['Set-Cookie']
    #cookie = re.match("'PHPSESSID':'(.+?)',.", cookies)
    #cookies.load(headers['Set-Cookie'])
    #print cookies
    #session = cookies['PHPSESSID'].value
    cookie = Cookie.SimpleCookie(r.headers['Set-Cookie'])
    sessionid = cookie['PHPSESSID'].value

    #js = json.loads(cookies)
    print "Headers:",r.headers
    #print "Cookies:",r.cookies
    #print "Raw:",r.raw
    #print "Set-Cookie:",r.headers['Set-Cookie']
    print "cookies:", cookies
    print "SessionID:", sessionid

    # Login
    print "--- Test Login ---"
    url = baseurl+"/login/login-ajax"
    #url = 'http://betanewwsh.vikduo.com/login/login-ajax'
    headers = headers
    postdata = {'captcha': captcha, 'username': username, 'password': password}
    cookies = {'PHPSESSID': sessionid}

    r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
    #length = len(r.text)
    #js = json.loads(r.text[1:length])

    print "headers:",r.headers
    print "Response:", r.content
    #print "Response:", r.text[1:length]
    print "length:", len(r.text)
