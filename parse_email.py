# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:30:00 2018

@author: U40MV02
"""
import re

def parse_email (s):
    """Parses a string as an email address, returning an (id, domain) pair."""
    e,d=s.split('@')
    x=re.search('^\D[\w.]+@[\w.-]+\D$',s)
    if not x:
        raise ValueError
    return (e,d)
    
    
print parse_email('richie@cc.gatech.edu7')
    
    
'''
    
    
def pass_case(u, d):
    s = u + '@' + d
    msg = "Testing valid email: '{}'".format(s)
    print(msg)
    assert parse_email(s) == (u, d), msg
    
pass_case('richie', 'cc.gatech.edu')
pass_case('bertha_hugely', 'sampson.edu')
pass_case('JKRowling', 'Huge-Books.org')

def fail_case(s):
    msg = "Testing invalid email: '{}'".format(s)
    print(msg)
    try:
        parse_email(s)
    except ValueError:
        print("==> Correctly throws an exception!")
    else:
        raise AssertionError("Should have, but did not, throw an exception!")
        
fail_case('x @hpcgarage.org')
fail_case('   quiggy.smith38x@gmail.com')
fail_case('richie@cc.gatech.edu  ')
fail_case('4test@gmail.com')
fail_case('richie@cc.gatech.edu7')'''