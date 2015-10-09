from lxml import etree
import time
import urllib2
from core.proxy import ProxyFactory

class _360Proxy(ProxyFactory):
    pageno = 1
    def FetchProxies(self):
#         baseURL = 'http://www.kuaidaili.com/free/inha/'
        baseURL = 'http://www.proxy360.cn/Region/China'
        # with open('r.txt', 'w') as c:
        #     c.write(content)
        proxies = []
        resp = urllib2.urlopen(baseURL)
        content = resp.read()
        resp.close()
#             with open('r.txt', 'w') as c:
#                 c.write(content)
        tree = etree.HTML(content)
        ipNodes = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_upProjectList"]/div/div[1]/span[1]')
        portNodes = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_upProjectList"]/div/div[1]/span[2]')
        for i,ip in enumerate(ipNodes):
            proxies += ["http://{0}:{1}".format(ip.text.strip(), portNodes[i].text.strip())]

        print("{0} fetched".format(len(proxies)))
        return proxies

if __name__ == '__main__':
    
#     for page in range(20, 50):
    start = time.time()
    p = _360Proxy()
    p.Run()
    end = time.time()
    print("total time:", end - start, "s")
    #print(pf.proxyPairs)
