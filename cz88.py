from lxml import etree
import time
import urllib2
from core.proxy import ProxyFactory

class cz88(ProxyFactory):
    pageno = 1
    def FetchProxies(self):
#         baseURL = 'http://www.cz88.com/free/inha/'
        baseURL = 'http://www.cz88.net/proxy/'
        # with open('r.txt', 'w') as c:
        #     c.write(content)
        proxies = []
        for page in range(1, 2):
            resp = urllib2.urlopen(baseURL + str(page))
            content = resp.read()
            resp.close()
#             with open('r.txt', 'w') as c:
#                 c.write(content)
            tree = etree.HTML(content)
            ipNodes = tree.xpath('//*[@id="boxright"]/div/ul/li/div[1]')
            portNodes = tree.xpath('//*[@id="boxright"]/div/ul/li/div[2]')
            for i,ip in enumerate(ipNodes):
                if i == 0:
                    continue
                proxies += ["http://{0}:{1}".format(ip.text.strip(), portNodes[i].text.strip())]

        print("{0} fetched".format(len(proxies)))
        return proxies

if __name__ == '__main__':
    
#     for page in range(20, 50):
    start = time.time()
    p = cz88()
    p.Run()
    end = time.time()
    print("total time:", end - start, "s")
    #print(pf.proxyPairs)
