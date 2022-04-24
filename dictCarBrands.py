brands={'H':'Honda','M':'Mazda'}
print brands
print brands['M']
model={'Honda':'Accord',"Mazda":"3"}
print model[brands['H']]
brands['B']='BMW'
print brands['B']
model['BMW']='328i'

for i,j in model.items():
	print "%s has car:%s" %(i,j)

print model.get("Audi")