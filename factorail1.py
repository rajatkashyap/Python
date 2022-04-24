i=int(raw_input("Enter a no: "))
mul=1
for x in range(i,1,-1):
	mul=mul*x
print mul	

mul=1
for j in range(2,i+1):
	mul=mul*j
print mul	

def fact(i):
	if i==1:
		return 1
	else: return i*fact(i-1)

print fact(5)