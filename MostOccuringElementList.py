# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:38:53 2019

@author: u40mv02
"""

s=[1,2,3,1,2,3,4,5,2,5,2,6,7,5,3,4,9,7,5,2,1]
cnt=0
elem=s[0]
for i in s:
    if s.count(i)>cnt:
        cnt=s.count(i)
        elem=i
print elem        

d={}
for i in s:
    d[i]=d.get(i,0)+1

print d

print sorted(d)
print sorted(d,reverse=True, key=d.get)[0]
print sorted(d.values(), reverse=True)