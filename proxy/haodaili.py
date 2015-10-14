from lxml import etree
import time
import urllib2
from core.proxy import ProxyFactory

class Haodaili(ProxyFactory):
    name = 'haodaili'
    def FetchProxies(self):
#         baseURL = 'http://www.Haodaili.com/free/inha/'
        # with open('r.txt', 'w') as c:
        #     c.write(content)
        proxies = []
        for page in range(1, 2):
            f = open('haodaili.txt')
            lines = f.readlines()
            for line in lines:
                proxies += ["http://{0}".format(line.strip())]

        print("{0} fetched".format(len(proxies)))
        return proxies

if __name__ == '__main__':
    
#     for page in range(20, 50):
    start = time.time()
    p = Haodaili()
    p.Run()
    end = time.time()
    print("total time:", end - start, "s")
    #print(pf.proxyPairs)
