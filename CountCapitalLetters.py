#Count Capital Letters
with open("CityPurchasesSumm.txt") as f:
	str=f.read()
	cnt=0
	for word in str:
		if word.isupper():
				cnt+=1
	print cnt
	
with open("CityPurchasesSumm.txt") as f:
	print [word.isupper() for word in f.read()]
	f.seek(0)
	cnt=sum(word.isupper() for word in f.read())
	print cnt
	

f=open("CityPurchasesSumm.txt")
str=f.read()
cnt=0
for word in str:
	if word.isupper():
		cnt+=1
print cnt
f.close()