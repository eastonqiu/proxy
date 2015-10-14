from proxy.cz88 import cz88
from proxy.ip66 import ip66
from proxy.kuaidaili import Kuaidaili
from proxy.proxy360 import Proxy360
from proxy.xicidaili import Xicidaili

# import MySQLdb


if __name__ == '__main__':
    proxyes = [Xicidaili(), ip66(), cz88(), Kuaidaili(), Proxy360()]
    
    with open('result.txt', 'w') as c:
        for p in proxyes:
            print(p.name)
            p.Run()
            print(p.proxyPairs)
            c.write(p.name + "\n")
            for pp in p.proxyPairs:
                c.write(str(pp[0]) + ',' + str(pp[1]) + '\n')
            c.write("\n")