import requests
import urllib
import urllib2
import re
#page=requests.get("https://en.wikipedia.org/wiki/For_loop")
aResp = urllib2.urlopen("https://en.wikipedia.org/wiki/For_loop");
#print page.text
web_pg = aResp.read();
f1=open('C:\Rajat\Python\HTMLread.txt','w')
f1.write(aResp.read());
f1.close()

#print web_pg
pattern='PERFORM VARYING'
m = re.search(pattern, web_pg)
print "\tCurrency:", m.group(1)


'''proxy_support = urllib2.ProxyHandler({"http":"http://61.233.25.166:80"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

html = urllib2.urlopen("http://www.google.com").read()
print html'''