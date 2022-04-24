import mechanize
import urllib2 
br = mechanize.Browser()
br.open("http://www.example.com/")
response1 = br.follow_link(text_regex=r"cheeses*shop", nr=1)
assert br.viewing_html()
print br.title()
print response1.geturl()
print response1.info()  # headers
print response1.read()  # body