from collections import OrderedDict
l=[1,2,2,1,6,1,2,5,4,2,3,6]
#print l
d=OrderedDict()
count=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

print d
for i in d:
    if d[i]==1:
        print i
        break

print [x for x in l if l.count(x)==1][0]  #first non-recurring letter
#print [x for x in range(10) if x%2==0]
counts=[]
for i in l:
    counts.append(l.count(i))
print counts
print [x for x in l if l.count(x)==max(counts)]  #prints all the occurrences of numbers which are repeating max times
#print [x for x in l if l.count(x)==max(l.count(x))]


