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

reducer()