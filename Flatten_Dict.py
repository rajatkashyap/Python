# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:23:55 2021

@author: U40MV02
"""

dict1={'a':{'b':'c','d':'e'},'1':{'2':'3','4':'5'}} 
#{a_b:c, a_d:e}
dict2={}
for key,value in dict1.items():
    for key1,value1 in value.items():
        dict2[key+'_'+key1]=value1
print (dict2)