import sys
import random
dict = {'Name': 'Rajat', 'City': 'Houston', 'Comp': 'AIG','Name':'Charu'}
dict1 = {'Name': 'Rajat', 'City': 'Houston', 'Comp': 'AIG','Name':'Charu'}
dict2 = {'Name': 'Rajat', 'City': 'Houston', 'Comp': 'AIG','Name':'Charu'}
print dict
print dict['Name']
dict['Country'] = 'US'
print dict['Country']
dict[1] = 'Fantastic'
print dict

states={'Texas':'TX','Arizona':'AZ'}
cities={'TX':'Houston','AZ':'Phoenix'}

print 'Texas: ', states['Texas']
print 'Texas: ',cities[states['Texas']]
print states.items()

for state,abbr in  states.items():
    print 'State %s is %s and has city %s' %(state,abbr,cities[abbr])

state = states.get('Utah','Does not exist')
print state
print dict['Name']
print len(dict)
print cmp(dict2,dict1)
print str(dict)
print dict
print type(dict)
dict4=dict.copy()
print dict4

print dict4.keys()
c=['city','City1','city2','city city']
print c.count('City')
for x in c:
    print x.capitalize()