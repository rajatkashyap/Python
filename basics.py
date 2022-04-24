# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:34:39 2019

@author: u40mv02
"""

print 10>20
n='Rajat\nKashyap'
print n

print "Let's talk abt %s" %n

l=[1,2,3, 5,5,10,10,5,3,2,4,1,0,9]
print l.count(5)
d=dict()
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print d

print [x for x in l if l.count(x)==1]

d={}
l2=[]
for i in l:
    if l.count(i)>1:
        if i not in l2:
            l2.append(i)
        
print l2