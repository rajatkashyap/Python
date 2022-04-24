from collections import OrderedDict
dict=OrderedDict()
dict['name']='Rajat'
dict['Age']=35
print dict
print dict.has_key('Age')
for i, j in dict.items():
    print i, j

print 'Rajat' in dict.values()
print 'name' in dict