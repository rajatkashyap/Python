# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 11:40:49 2018

@author: U40MV02
"""

import re
pattern='raj'
pattern=re.compile(pattern)
input='ccccrajat is great raj is great and raj'
mat=pattern.search(input)
print mat
print mat.group()
print mat.start()
print mat.end()
print mat.span()
