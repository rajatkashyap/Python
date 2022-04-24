from mechanize import urlopen, urljoin
import cookielib
import urllib2 

br=mechanize.Browser()
br.open("http://www.thetimenow.com/india")
print br.title()