# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 11:55:32 2018

@author: U40MV02
"""

import re
input='raj@at. raj@t is great raja 123  1      34is great and raj'
mat=re.search('raj',input)
mat1=re.findall('raj',input)
#mat2=re.match('rajat',input)
#print mat.span()
#print mat1.groups()
#print mat2.groups() 
x=re.search('..j',input)
print x.group()
x=re.search('..j...\.',input)
print x.group()
x=re.search('..j.',input)
print x.group()
x=re.search('\w\w\w\wt',input)
print x.group()
x=re.search(r'\d\d\d',input)
print x.group()
x=re.search(r'\d\s+\d\d',input)
print x.group()
x=re.search(r'@\w+[a-z]',input)
print x.group()
x=re.search('^([a-zA-Z]+)\s([a-zA-Z]+)','Rajat Kashyap')
print x.groups()