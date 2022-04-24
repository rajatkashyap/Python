def get_time(l):
	if len(l)==1:
		return l[0][1]-l[0][0]
	new_l=[]
	'''for i in range(len(l)-1):
		if l[i+1][0]<=l[i][1]:
				new_l.append((l[i][0],l[i+1][1]))'''
	print 'Before'			
	if l[1][0]<=l[0][1]:
		new_l.append((l[0][0],l[1][1]))
	else:
		new_l.append(l[0])
		new_l.append(l[1])
	new_l=new_l+l[2:]
	print new_l
	print 'After'
	return get_time(new_l)		
	
l=[(0,30),(32,60),(65,90),(50,85),(90,120)]
print l
l1=sorted(l)
print "After sort:" ,l1
print get_time(l1)


