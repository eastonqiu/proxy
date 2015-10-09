import time
import multiprocessing
from multiprocessing import Process, Queue
import urllib2
from lxml import etree

class Proxy:
    def __init__(self, addr, time):
        self.address = addr
        self.time = time
    def __lt__(self, other):
        return self.time < other.time

class ProxyFactory:

    def __init__(self):
        
        self.pool = []
        self.proxyPairs = []
    
    def Run(self):
        proxyList = self.FetchProxies()

        #print(proxyList) 
        
        self.ValidateProxies(proxyList)
        
        self.pool.sort()
        
        for i in self.pool:
            self.proxyPairs += [(i.address, i.time)]


    def FetchProxies(self):
        # user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        # headers = { 'User-Agent' : user_agent }
        # baseURL = 'http://www.xicidaili.com/nn/'
        # proxies = []
        # for page in range(1, 6):
        #     req = urllib2.Request(baseURL + str(page), None, headers)
        #     resp = urllib2.urlopen(req)
        #     content = resp.read()
        #     resp.close()
        #     tree = etree.HTML(content)
        #     ipNodes = tree.xpath('//*[@id="ip_list"]/tr/td[3]')
        #     portNodes = tree.xpath('//*[@id="ip_list"]/tr/td[4]')
        #     typeNodes = tree.xpath('//*[@id="ip_list"]/tr/td[7]')
        #     for i,type in enumerate(typeNodes):
        #         if(type.text.strip() == 'HTTP'):
        #             #print ipNodes[i].text.strip() + ":" + portNodes[i].text.strip()
        #             proxies += ["http://{0}:{1}".format(ipNodes[i].text.strip(), portNodes[i].text.strip())]
        
        # #print proxies
        # print("{0} fetched".format(len(proxies)))
        # return proxies
        return None
    
    def CheckProxy(self, address, tests, result):
        for t in tests:
            proxy=urllib2.ProxyHandler({'http': address})
            opener=urllib2.build_opener(proxy)
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36')]
            urllib2.install_opener(opener)
            try:
                start = time.clock()
                #data = opener.open(url = t, timeout = 5).read().decode()
                #data = opener.open(t, timeout = 5).read().decode()
                content = urllib2.urlopen(t, timeout=5)
                content.read()
                #print sContent.read()
                end = time.clock()
                #print("[Proxy {0}]: OK for {1} in time: {2} s".format(address, t, end - start))
                result.put((address, end - start))
            except Exception as e:
                #print(e)
                #print("[Proxy {0}]: not available".format(address))
                pass
    
    def ValidateProxies(self, proxyList):
            
        maxProc = 50
        
        tests = ["http://www.baidu.com"]
    
        result = Queue()
       
        start = time.clock()
        
        for i in proxyList:
            p = Process(target=self.CheckProxy, args=(i, tests, result))
            p.start()  
            
            if len(multiprocessing.active_children()) > maxProc:
                #print('active_children: ', multiprocessing.active_children())
                p.join()
            
        while len(multiprocessing.active_children()) > 0:
            time.sleep(3)
        end = time.clock()
        #print("total time for validation:", end - start, "s")
        
        self.pool = []
        
        for i in range(result.qsize()):
            a = result.get()
            self.pool += [Proxy(a[0], a[1])]

        
        print("{0} validated".format(len(self.pool)))

    


if __name__ == '__main__':
    pf = ProxyFactory()
    pf.Run()
    print(pf.proxyPairs)
    #with open('r.txt', 'w') as c:
    #c.write(pf.proxyPairs)
