# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:19:45 2018

@author: U40MV02
"""
import re
def find(pat,txt):
    n=re.search(pat,txt)
    if n:
        print n.group()
    else:
        print ("Not found")
        
find(r':\w+','rajat:kashyap')
find(r'\d\s+\d','1    4  4')
email='bla blah hdslkhs rajat.kas@gmail.com  few;lewuw yy22@@'
e=re.search(r'\w[\w.]+@[\w.]+',email)
print (e.group())
 
email='bla blah hdslkhs rajat.kas@gmail.com  few;lewuw yy22@@ yahoo.com'
e=re.search(r'(\w[\w.]+@[\w.]+).*\s+([\w]*[.]\w*)$',email)
print (e.groups())

