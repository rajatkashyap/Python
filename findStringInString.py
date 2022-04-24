def findstring(s1,s2):
	l1=len(s1)
	l2=len(s2)
	c=0
	for i in range(0,l1):
		print s1[i:i+l2]
		if s1[i:i+l2]==s2:
			c+=1
		else:
			continue
	return c
			
s1=raw_input("Enter main string: ")
s2=raw_input("Enter string to find: ")
counter=findstring(s1,s2)		
			
print "String appeared %d times" %counter

