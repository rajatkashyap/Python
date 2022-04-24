s=[10,4,7,3, 5,8,8,7,1,2,7, 5, 3, 3,3,5, 7, 3,5, 5, 5,7,7,3]
dict={}
for i in s:
	if i in dict: dict[i]+=1
	else: dict[i]=1
print dict

dict1={}
for i in s:
	dict1[i]=dict1.get(i,0)+1

print dict1

# finding the first non-recurring
for elem in s:
	if dict[elem]==1:
		print "first non-recurring %d with %d occurances" %(elem,dict[elem])
		break

# finding the most-recurring
print "Using dict.get"
print max(dict,key=dict.get)

print "Using lambda "
print max(dict,key=lambda x:dict[x])

print "Using dict[i]==max(counts)"
counts=[]
for i in s:
	counts.append(s.count(i))
for i in dict:
	if(dict[i]==max(counts)):
		print i
		break
		
print "s[counts.index(max(counts))]"
print s[counts.index(max(counts))]

val=list(dict.values())
keys=list(dict.keys())

print "Using keys[val.index(max(val))]"
print keys[val.index(max(val))]


# finding the first most-recurring
print counts
for i in s:
	if s.count(i)==max(counts):
		print i
		break

		
'''
print max(dict,key=lambda x:dict[x])

val=list(dict.values())
keys=list(dict.keys())

print keys[val.index(max(val))]

print max(dict,key=dict.get)

print dict.get(7)

dict1={}

for i in s:
    dict1[i]=dict1.get(i,0)+1

print max(dict1, key=dict1.get)'''