# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:39:47 2019

@author: u40mv02
"""
s=0
c=0
i=0
while i!=-1:
    i=float(raw_input("Enter a no, -1 to exit:"))
    if i==-1: break
    s=s+i
    c+=1
print s/c

s=[]
while i!=-1:
    i=float(raw_input("Enter a no, -1 to exit:"))
    s.append(i)
    
print s.avg()


