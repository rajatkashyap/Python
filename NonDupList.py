# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:08:49 2021

@author: U40MV02
"""

l=[1,1,3,2,5,6,5] 
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
        
print (l1)

l2=[1,2,3,[4,5,6],7,8,[9,10]]
l3=[]
for i in l2:
    if type(i) is list:
        for j in i:
            l3.append(j)
    else:
        l3.append(i)

print (l3)


l4=[]
for i in l2:
    if isinstance(i,list):
        for j in i:
            l4.append(j)
    else:
        l4.append(i)

print (l4)

assert l3==l4, "Not matching"



