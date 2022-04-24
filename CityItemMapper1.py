def mapper():
	f1=open("purchases.txt")
	l=f1.readlines()
	
	f2=open("CityPurchases1.txt","w")
	for line in l:
		#print line
		data=line.split('\t')
		date,time,city,item,price,card=data
		f2.write("{0}\t{1}\n".format(city,price))
	f1.close()
	f2.close()
def sorter():
	f3=open('CityPurchases1.txt')
	f4=open("CityPurchasesSorted1.txt","w")
	data=f3.readlines()
	data.sort()
	for line in data:	
		f4.write(line)
	f3.close()
	f4.close()

def reducer():
	f5=open('CityPurchasesSorted1.txt')
	dict_city={}
	data=f5.readlines()
	for line in data:
		fields=line.strip().split('\t')
		city,price=fields
		#print city,price
		if city in dict_city:
			#print dict_city[city]
			dict_city[city]=dict_city[city]+float(price)
		else:
			dict_city[city]=float(price) 
	print dict_city	
	for k,v in  dict_city.items():
		print k,v
		
	
mapper()
sorter()
reducer()
