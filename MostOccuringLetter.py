txt=raw_input('Enter some text: ')
txt=txt.lower().replace(' ','')
l=[]
for i in txt:
	l.append(txt.count(i))
print l	
maxi=max(l)
print txt[l.index(max(l))]



for i in range(0,len(l)):
	if l[i]==maxi:
		print txt[i]
		break

