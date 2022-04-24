# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:59:21 2021

@author: U40MV02
"""

l1=[1,2,3,3,1,1,1]
l2=[1,1,2,2,3] 
l=[]
for i in l1:
    if i in l2 and i not in l:
        l.append(i)
l.sort()
print (l)