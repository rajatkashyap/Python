import math
def smaller_root(a,b,c):
	d=(b**2)-(4*a*c)
	if d<0:
		print "Error: No real solutions"
		return
	elif d==0:
		return -(b/2*a)
	else:
		s1=(-b-math.sqrt(d))/2*a
		s2=(-b+math.sqrt(d))/2*a
		if s1<s2: 
			return s1 
		else:
			return s2 
			

print smaller_root(-1,4,3)

