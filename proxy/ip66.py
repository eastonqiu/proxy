from lxml import etree
import time
import urllib2
from core.proxy import ProxyFactory

class ip66(ProxyFactory):
    name = '66ip'
    def FetchProxies(self):
#         baseURL = 'http://www.66ip.com/free/inha/'
        baseURL = 'http://www.66ip.cn/'
        # with open('r.txt', 'w') as c:
        #     c.write(content)
        proxies = []
        for page in range(1, 20):
            resp = urllib2.urlopen(baseURL + str(page) + '.html')
            content = resp.read()
            resp.close()
#             with open('r.txt', 'w') as c:
#                 c.write(content)
            tree = etree.HTML(content)
            ipNodes = tree.xpath('//*[@id="footer"]/div/table/tr/td[1]')
            portNodes = tree.xpath('//*[@id="footer"]/div/table/tr/td[2]')
            for i,ip in enumerate(ipNodes):
                if i == 0:
                    continue
                proxies += ["http://{0}:{1}".format(ip.text.strip(), portNodes[i].text.strip())]

        print("{0} fetched".format(len(proxies)))
        return proxies

if __name__ == '__main__':
    
#     for page in range(20, 50):
    start = time.time()
    p = ip66()
    p.Run()
    end = time.time()
    print("total time:", end - start, "s")
    #print(pf.proxyPairs)
