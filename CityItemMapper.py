def mapper():
	p=open("purchases.txt")
	p1=open("CityPurchases.txt","w")
	for line in p:
		data=line.strip().split("\t")
		date,time,city,item,price,card=data
		if len(data)==6:
			p1.write("{0}\t{1}\n".format(city,price))
	p1.close()
	p.close()
	
def sorter():
	p=open("CityPurchases.txt")
	p1=open("CityPurchasesSorted.txt","w")
	lines=p.readlines()
	lines.sort()
	for line in lines:
		p1.write(line)
	p1.close()
	p.close()

def reducer():
	f=open("CityPurchasesSorted.txt")
	f1=open("CityPurchasesSumm.txt","w")
	salestotal=0
	oldcity=None
	for line in f:
		data=line.strip().split("\t")
		city,price=data
		if oldcity and oldcity!=city:
			f1.write("{0}\t{1}\n".format(oldcity,salestotal))
			salestotal=0
		oldcity=city 
		salestotal=salestotal+float(price)
	f1.write("{0}\t{1}\n".format(oldcity,salestotal))
	f1.close()
	f1.close()

mapper()
sorter()
#reducer()
	