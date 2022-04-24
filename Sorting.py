	#5 3 9 0
l=raw_input("Enter nos: ")
l=l.split()
min=int(l[0])
min_l=[]
while l:
	min=int(l[0])
	for y in l:
		y=int(y)
		if y<min:
			print y
			min=y
	print min		
	min_l.append(min)
	#l.remove(str(min))
	print l
print min_l

