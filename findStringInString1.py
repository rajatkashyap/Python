s1=raw_input("Main string: ") 
s2=raw_input("Find the string: ") 
l1=len(s1)
l2=len(s2)
counter=0
for i in range(l1):
	if s1[i:i+l2]==s2:
		counter+=1

print "String appears %d times" %counter