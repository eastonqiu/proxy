from lxml import etree
import time
import urllib2
from core.proxy import ProxyFactory

class Xicidaili(ProxyFactory):
    pageno = 1
    def FetchProxies(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        headers = { 'User-Agent' : user_agent }
        baseURL = 'http://www.xicidaili.com/nn/'
        proxies = []
        for page in range(1, 101):
            req = urllib2.Request(baseURL + str(page), None, headers)
            resp = urllib2.urlopen(req)
            content = resp.read()
            resp.close()
#             with open('r.txt', 'w') as c:
#                 c.write(content)
            tree = etree.HTML(content)
            ipNodes = tree.xpath('//*[@id="ip_list"]/tr/td[3]')
            portNodes = tree.xpath('//*[@id="ip_list"]/tr/td[4]')
            typeNodes = tree.xpath('//*[@id="ip_list"]/tr/td[7]')
            for i,t in enumerate(typeNodes):
                if(t.text.strip() == 'HTTP'):
                    #print ipNodes[i].text.strip() + ":" + portNodes[i].text.strip()
                    proxies += ["http://{0}:{1}".format(ipNodes[i].text.strip(), portNodes[i].text.strip())]

        print("{0} fetched".format(len(proxies)))
        return proxies

if __name__ == '__main__':
    
#     for page in range(20, 50):
    start = time.time()
    p = Xicidaili()
    p.Run()
    end = time.time()
    print("total time:", end - start, "s")
    #print(pf.proxyPairs)
