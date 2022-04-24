names={}
names1={}
n=['Rajat','Parag','Charu','Charu','Rajat','Parag','Barkha','Rajat']
for name in n:
	names[name]=names.get(name,0) +1
    
    
for name in n:
    if name in names1:
        names1[name]=names1[name]+1
    else:
        names1[name]=1
print (names)
print (names1)

print (sorted(names))

		