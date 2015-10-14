from lxml import etree
import time
import urllib2
from core.proxy import ProxyFactory

class Kuaidaili(ProxyFactory):
    name = 'kuaidaili'
    def FetchProxies(self):
#         baseURL = 'http://www.kuaidaili.com/free/inha/'
        baseURL = 'http://www.kuaidaili.com/free/intr/'
        # with open('r.txt', 'w') as c:
        #     c.write(content)
        proxies = []
        for page in range(1, 20):
            resp = urllib2.urlopen(baseURL + str(page))
            content = resp.read()
            resp.close()
#             with open('r.txt', 'w') as c:
#                 c.write(content)
            tree = etree.HTML(content)
            ipNodes = tree.xpath('//*[@id="list"]/table/tbody/tr/td[1]')
            portNodes = tree.xpath('//*[@id="list"]/table/tbody/tr/td[2]')
            typeNodes = tree.xpath('//*[@id="list"]/table/tbody/tr/td[4]')
            for i,t in enumerate(typeNodes):
                if(t.text.strip() == 'HTTP'):
                    #print ipNodes[i].text.strip() + ":" + portNodes[i].text.strip()
                    proxies += ["http://{0}:{1}".format(ipNodes[i].text.strip(), portNodes[i].text.strip())]

        print("{0} fetched".format(len(proxies)))
        return proxies

if __name__ == '__main__':
    
#     for page in range(20, 50):
    start = time.time()
    p = Kuaidaili()
    p.Run()
    end = time.time()
    print("total time:", end - start, "s")
    #print(pf.proxyPairs)
