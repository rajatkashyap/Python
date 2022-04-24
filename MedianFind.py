list1=raw_input("Enter list of nos")
list2=list1.split()
list2.sort()
length=len(list2)

if length%2==1:
	print list2[length/2]
else:
	print (int(list2[(length/2)-1])+int(list2[(length/2)]))/2.0