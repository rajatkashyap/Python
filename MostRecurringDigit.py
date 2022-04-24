s=[3,4,5,7,8,8,7,1,2,3,7, 5, 3, 5, 7, 5, 5, 5]
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print dict

print max(dict,key=lambda x:dict[x])

val=list(dict.values())
keys=list(dict.keys())

print keys[val.index(max(val))]

print max(dict,key=dict.get)

print dict.get(7)

dict1={}

for i in s:
    dict1[i]=dict1.get(i,0)+1

print max(dict1, key=dict1.get)