# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:39:17 2018

@author: U40MV02
"""
from itertools import accumulate
def get_obstruction(X, h):
    
    for i in range(len(X)):
        if X[i]>=h:
            pos=i
            break
    
    #print (pos)
    l=len(X)
    pos_l=[1 for i in range(0,l-1)]
    #print (pos_l)
    acc_l=list(accumulate(pos_l))
    #print (acc_l)
    return  (acc_l[pos-1:])
h=5 
X=[6, 6, 9, 3, 1, 3, 1, 1, 8]
print get_obstruction(X,h)