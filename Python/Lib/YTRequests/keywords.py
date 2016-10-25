# encoding: utf-8
import requests,re,json
from version import VERSION

class ReqLib(object):
    ss = requests.Session()
    url = None
    urldict = {}
    alias = 'alias'
    ssdict = {}

    def __init__(self):
       pass

    def version(self):
        print "Version:%s" % VERSION

    def get_request(self,alias, url, headers={},cookies={}):
        """
        Get请求

        示例：${resp} |	Get Request	| wsh	| /login/index

        :param alias: session名称
        :param url: 请求地址,如: /shop-ajax
        :param headers:
        :param cookies:
        :return:
        """
        print "-- Info: Get Request --"
        ss = self.ssdict.get(alias)
        baseurl = self.urldict.get(alias)
        url = baseurl + url

        if ss == None:
            print "Wrong alias."
            return None
        r = self.ss.get(url=url,headers=headers)
        return r

    def post_request(self,alias, url,data=None, headers={}, cookies={}):
        """
        Post请求

        示例：${resp} |	Post Request	| sub	| /terminal/list-ajax

        :param alias:
        :param url:
        :param data:
        :param headers:
        :param cookies:
        :return:
        """
        print "-- Info: Post Request --"
        ss = self.ssdict.get(alias)
        baseurl = self.urldict.get(alias)
        #print "baseurl:%s" % baseurl
        url = baseurl + url
        #print "url:%s" % url

        if ss == None:
            print "Wrong alias."
            return None
        r = self.ss.post(url=url, data=data, headers=headers)
        return r

    def create_session(self, name, url, cookies={}):
        """
        创建Session
        示例：

        Create Session | wsh	| http://betanewwsh.snsshop.net

        Create Session | sub	| http://betashopadmin.snsshop.net	| cookies=${cookies}

        :param name:
        :param url:
        :param cookies:
        :return:
        """
        print "-- Info: Create Session --"
        flag_ss = self.ssdict.get(name)
        flag_url = self.urldict.get(name)
        if flag_ss == None:
            try:
                resp = self.ss.get(url=url,cookies=cookies)
                self.url = url
                #print "session resp:%s" % resp.text
                #x = 1
            except Exception:
                print "errors... %s" % Exception.message
            self.ssdict[name] = self.ss
            self.urldict[name] = url
        else:
            print "%s already exist."
        return self.ss

    def simple_session(self,url=None):
        self.ss.get(url=url)

    def get_cookie(self,alias,name):
        """
        获取Cookie

        :param alias:
        :param name:
        :return: cookie
        """
        print "-- Info Get Cookie --"
        ckjar = self.ss.cookies
        #str1 = str(ckjar)
        #ck = ckjar._cookies
        #print "ck:",str1
        #match = re.findall(r'(?<=http://).*',self.url)
        match = re.findall(r'(?<=PHPSESSID=).*(?=\sfor)',str(ckjar))
        cookie = match[0]

        #beta = ck[domain]
        #baseck = beta['/']
        #cookie = baseck[name]   # cookie keyname

        return cookie

    def json_loads(self,jsondata):
        """
        加载JSON数据

        :param jsondata:
        :return:
        """
        print "-- Info Load From Json --"
        data = json.loads(jsondata)
        #print "data:",data

        return data



# def keywords


