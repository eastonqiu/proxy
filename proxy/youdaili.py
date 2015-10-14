from lxml import etree
import re
import time
import urllib2

from core.proxy import ProxyFactory


class Youdaili(ProxyFactory):
    name = 'youdaili'
    def FetchProxies(self):
        proxies = []
        
        baseURL = 'http://www.youdaili.net/Daili/guonei/3704.html'
#         user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36'
        headers = { 'User-Agent' : user_agent, 'Cookie':'BAIDU_DUP_lcr=https://www.baidu.com/link?url=ILXXGeokSMN_7s3kRO8r9lEFzdt68SOyC6mwFHx1m5HuC9JkLFSJVPlJNtP55KTC&wd=&eqid=ae39bf2d00001f41000000055617aef2; Hm_lvt_f8bdd88d72441a9ad0f8c82db3113a84=1444392700; Hm_lpvt_f8bdd88d72441a9ad0f8c82db3113a84=1444394742'}
        req = urllib2.Request(baseURL, None, headers)
        resp = urllib2.urlopen(req)
#         resp = urllib2.urlopen(baseURL)
        content = resp.read()
        resp.close()
        results = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', content)
        print results
        for ipport in results:
            proxies += ["http://{0}".format(ipport)]

        print("{0} fetched".format(len(proxies)))
        return proxies

if __name__ == '__main__':
    
#     for page in range(20, 50):
    start = time.time()
    p = Youdaili()
    p.Run()
    end = time.time()
    print("total time:", end - start, "s")
    #print(pf.proxyPairs)
