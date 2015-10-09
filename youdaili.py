from lxml import etree
import re
import time
import urllib2

from core.proxy import ProxyFactory


class Youdaili(ProxyFactory):
    pageno = 1
    def FetchProxies(self):
        proxies = []
        
        baseURL = 'http://www.youdaili.net/Daili/guonei/3704.html'
#         user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
#         headers = { 'User-Agent' : user_agent }
#         req = urllib2.Request(baseURL, None, headers)
#         resp = urllib2.urlopen(req)
        resp = urllib2.urlopen(baseURL)
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
