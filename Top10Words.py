f=open('UHC.txt')
dict={}
words=f.read().split()

for word in words:
	w=word.lower()
	dict[w]=dict.get(w,0)+1
		

#print dict

str_tups=[]
for k,v in dict.items():
	str_tups.append((v,k))

#print str_tups

str_tups.sort(reverse=True)

print str_tups[:10]

keys=dict.keys()
values=dict.values()
#print keys 
#print values 
values.sort(reverse=True)

for i in range(10):
	for key in keys:
		if dict[key]==values[i]:
			print key,values[i]


'''
for i in range(10):
	for d in dict:
		if d[keys[i]]==values[i]:
			print d '''