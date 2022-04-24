f=open('UHC.txt')
dict={}
data=f.readlines()

for line in data:
	for word in line:
		w=word.lower()
		dict[w]=dict.get(w,0)+1
		
		
print dict