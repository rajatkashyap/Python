import re
from sys import argv
s,p,t=argv
def find(pattern,text):
	m=re.search(pattern,text)
	if m: print m.group()
	else: print 'Not found'
	

	
find(p,t)	

	
	
	
