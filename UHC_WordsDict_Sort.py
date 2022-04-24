# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:50:02 2019

@author: u40mv02
"""

f=open("UHC.txt")
d={}
for line in f:
    line_l=line.split()
    for word in line_l:
        d[word]=d.get(word,0)+1

d1=sorted(d,reverse=True, key=d.get)
print d[d1[0]]
new=[]
for k,v in d.items():
    new.append((v,k))

new.sort(reverse=True)
print new[0][1]
