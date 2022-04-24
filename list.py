from collections import OrderedDict
a=[4,3,2,8,9,6,7,1,7,9,6,4,7]
print max(a)

non=[1,2,1,1,2,1,7,5,4,3,7]
l=len(a)

print a
s= list(set(a))
print s
s.sort(reverse=True)
print s
print s[1]

if (l%2==0):
    m=(a[(l/2)-1] + a[(l/2)])/2.0
else:
    m=a[l//2]

print m

print '*'*35
counts=OrderedDict()
for i in non:
    if i not in counts:
        counts[i]=1
    else:
        counts[i] += 1

print counts
for i in counts:
    if counts[i]==1:
        print i
        break

counts=[]



