# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:02:04 2021

@author: U40MV02
"""

s="Hi how are you doing today Rajat How is your day going today rajat"
l=s.split()
counts={}
for i in l:
    i=i.lower()
    if i in counts:
        counts[i]=counts[i]+1
    else:
        counts[i]=1
print (counts)

counts1={}
for i in l:
    i=i.lower()
    counts1[i]=counts1.get(i,0)+1
print (counts1)