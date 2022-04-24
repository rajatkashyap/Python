# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:58:07 2018

@author: U40MV02
"""

def is_ssn(s):
    if s[3:4]!='-' or s[6:7]!='-':
        return False
    if len(s)!=11: 
        return False
    s=s.replace('-','')
    if not(s.isdigit()):
        return False
    return True

def is_ssn3(s):
    if s[3:4]!='-' or s[6:7]!='-':
        return False
    if len(s)!=11: 
        return False
    l_s=s.split('-')
    for i in l_s:
        if not(i.isdigit()):
            return False
        return True


def is_ssn2(s):
    parts=s.split('-')
    length=[3,2,4]
    if len(parts)!=len(length): 
        return False
    for p,n in zip(parts,length):
        print (p,n)
        if not(p.isdigit() and len(p)==n):
            return False
    return True
        
    

assert is_ssn('123-45-6789'), 'Nopes!'
#assert is_ssn2('123-45-67819'), 'Nopes!!!!'
assert is_ssn3('123-57-6789'), 'Nopes!'