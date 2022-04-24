nos=raw_input("enter nos")
nos=nos.split()
largest=None 
smallest=None

for no in nos:
	if smallest is None or largest is None:
		smallest=int(no)
		largest=int(no)
	elif int(no)<smallest: 
		smallest=int(no)
	elif int(no)>largest:
		largest=int(no)
	print "Largest:", largest
	print "Smallest:", smallest
 
print '*'*10	
print "Largest:", largest
print "Smallest:", smallest
