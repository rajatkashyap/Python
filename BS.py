import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://espn.go.com/college-football/standings’).read())

for row in soup('table', {'class': 'standings has-team-logos’})[0].tbody('tr'):
    tds = row('td')
    print tds[1].string, tds[0].string