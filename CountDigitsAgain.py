s=[1,1,2,2,2,2,3,3,2,1,6,7,5]
cnt=[]
for i in s:
    cnt.append(s.count(i))

for i in cnt:
    if i ==1:
        print s[cnt.index(i)]
        break

print [x for x in s if s.count(x)==1][0]

d={}
from collections import OrderedDict
d1=OrderedDict()
for i in s:
    if i in d:
        d[i]=d[i]+1
        d1[i] = d1[i] + 1
    else:
        d[i] = 1
        d1[i] = 1

print d
print '*'*10
print s
print max(d1,key=d.get)
print min(d1,key=d.get)

print '*'*10
print d.values()
print d.keys()
for i,j in d.items():
    print i,j

print d1
d1={}
for i in d:
    if d[i]==1:
        d1[i]=d[i]

print d1

for i in s:
    if i in d1:
        print i
        break
		
for n in names:
    if names[n]==max(names.values()):
            print n

			
			
>>> name1=None
>>> name_count=None
>>> for n,c in names.items():
...     if name_count is None or name_count<c:
...             name1=n
...             name_count=c
...
>>> print name_count,name1
3 Rajat			
