# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:56:10 2018

@author: U40MV02
"""
import re
def parse_phone1 (s):

    
    re_p = re.compile ('''^
                           (?P<area>\s*\(\d\d\d\))
                           \s*
                           (?P<first>\d\d\d)
                           -
                           (?P<last>\d\d\d\d\s*)
                           $
                        ''',
                        re.VERBOSE)
       
    a=re_p.match(s)#.group('area')
    f=re_p.match(s)#.group('first')
    l=re_p.match(s)#.group('last')
    if not a or not f or not l:
        raise ValueError
       
    return (a.group('area').strip()[1:-1],f.group('first'),l.group('last').strip())
#re_p = re.compile('^(?P<area>\s*\(\d\d\d\))')
#print re_p.match('(123)456-7878').group('area')
#print  parse_phone1('(123)456-7878')
print  parse_phone1('    (304)    528-5826    ')
