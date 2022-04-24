def find_s(s1,s2):
	cnt=0
	l1=len(s1)
	l2=len(s2)
	for i in range(l1):
		if s1[i:i+l2]==s2:
			print (s1[i:i+l2])
			cnt+=1
	return cnt		
print (find_s('atRatjatat','at'))