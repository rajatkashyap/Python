input=raw_input("Enter two nos")
l=[int(x) for x in input.split(',')]
arr1=[]
for i in range(l[0]):
	arr=[]	
	for j in range(l[1]):
		arr.append(i*j)
	arr1.append(arr)

print arr1