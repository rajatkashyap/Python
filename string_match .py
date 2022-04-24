# -*- coding: utf-8 -*-
"""

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""

def string_match(a, b):
  if len(a)<=len(b):
    l=len(a)
  else:
    l=len(b)
  cnt=0
  for i in range(l-1):
    if a[i:i+2]==b[i:i+2]:
        print a[i:i+2]
        print '*'
        print b[i:i+2]
        cnt+=1
  return cnt

print string_match('xxcaazz', 'xxbaaz')