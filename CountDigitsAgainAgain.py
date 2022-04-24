from collections import OrderedDict
l=[10,11,10,10 ,1,2,2,1,6,1,2,5,4, 4,4,4, 10 ,11,10]
dict={}
od=OrderedDict()
for i in l:
	if i in dict:
		dict[i]=dict[i]+1
	else:
		dict[i]=1

print dict		
for i in l:
	if i in od:
		od[i]=od[i]+1
	else:
		od[i]=1

print od	


print max(dict,key=dict.get)

abc=[]
for i in dict:
	abc.append(dict[i])
	
abc.sort(reverse=True)
max_val=abc[0]


for i in dict:
	if dict[i]==max_val:
		print i
		break
	
	


		