from lxml import etree
import re
import urllib2

def printText(node):
    ip = ''
    if(len(node.items()) > 0 and len(node.items()[0]) >= 2 and node.items()[0][0] == 'style' and 'none' in node.items()[0][1]):
        return ''
    if(node.text != None):
        ip += node.text
    else:
        for subnode in node.getchildren():
            ip += printText(subnode)
    return ip

baseURL = 'http://proxy.goubanjia.com/free/'
# user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# headers = { 'User-Agent' : user_agent }
# req = urllib2.Request(baseURL, None, headers)
# resp = urllib2.urlopen(req)
# resp = urllib2.urlopen(baseURL)
# content = resp.read()
# resp.close()
# with open('r.txt', 'w') as c:
#     c.write(content)
# ret = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', content)
# print ret
    
# tree = etree.HTML(content)
# ipNodes = tree.xpath('//*[@id="list"]/table/tbody/tr/td[1]')
# portNodes = tree.xpath('//*[@id="list"]/table/tbody/tr/td[2]')
# 
# for node in ipNodes:
#     ip = printText(node)
#     print ip
    