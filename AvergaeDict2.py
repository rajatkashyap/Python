counter=int(raw_input("How many elements"))
dict={}
for i in range(counter):
	row=raw_input().split()
	int_row=[]
	for x in range(1,len(row)):
		int_row.append(int(row[x]))
	print int_row	
	print sum(int_row)
	dict[row[0]]=sum(int_row)/(len(int_row)*1.0)
print dict	
		

