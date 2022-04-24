# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:20:46 2019

@author: u40mv02
"""

dict1={}
dict1={"name":"Rajat","city":"Houston","make":"Honda"}
print (dict1)
#dict.popitem()
x = ['key1', 'key2', 'key3']
y =[1,2,3]

#print (dict1.has_key('key1'))
#print dict1.get("city")
#print dict1["city"]

for d in dict1:
    print (d)

print ("***")

#p= dict1.iterkeys()
for p1 in dict1.keys():
    print( p1)
    
for p1 in dict1.values():
    print( p1)
    
print ("***")
    
for i,j in dict1.items():
    print( i)
    print (j)

print ("***")
    
d1=sorted(dict1,key=dict1.get)
print (d1)


dict1.sort()
print (dict1)


    
'''    
print "***"

for i in dict1.itervalues():
    print i

print "***"

thisdict = dict.fromkeys(x, y)
print thisdict

#dict_new=dict(x=5, y=0)
#print dict_new

print [(i,j) for i in range(0,10) for j in range(0,5)]

for i,j in dict1.items():
    print "%s has value:%s" %(i,j)
    print i,j

for i,j in dict1.items():
    print (i,j)

d1=sorted(dict1,key=dict1.get)
print "***"
print d1


new_d=dict()
print new_d

state={'Oregon':'OR','Florida':'FL'}
city={'FL':'Miami'}
print city[state['Florida']]
print state

#print state['Texas']
print state.get('Texas','Not in States Dictionary')
'''