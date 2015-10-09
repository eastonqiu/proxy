from lxml import etree
import re
import urllib2

baseURL = 'http://www.youdaili.net/Daili/guonei/3704.html'
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request(baseURL, None, headers)
resp = urllib2.urlopen(req)
# resp = urllib2.urlopen(baseURL)
content = resp.read()
resp.close()
with open('r.txt', 'w') as c:
    c.write(content)
ret = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', content)
print ret
    
# tree = etree.HTML(content)
# ipNodes = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_upProjectList"]/div/div[1]/span[1]')
# portNodes = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_upProjectList"]/div/div[1]/span[2]')
# 
# for node in ipNodes:
#     print node.text.strip()