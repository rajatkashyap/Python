import math
i=raw_input("Enter numbers")
l=i.split()
out=[]
c=50
h=30
for i in l:
	out.append(int(round(math.sqrt((2*c*int(i))/h))))
print out
	
