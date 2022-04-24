d= {}
x_______1 = [0,1,2,3,4,5,6,7]
d['inds'] = [0,   3,   7,   3,   3,   5, 1]
d['vals'] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
x_true = [1.0, 7.0, 0.0, 11.0, 0.0, 6.0, 0.0, 3.0]
#print d

def decompress_vector(d, n=None):
	lt=[]
	if n is None: 
		l=max(d['inds'])+1
	else:
		l=n

	new=[]
	new_vals=[]
	for i in d['inds']:
		if i not in new:
			new.append(i)
			new_vals.append(d['vals'][d['inds'].index(i)])
		else:
			new_vals.append(d['vals'][d['inds'].index(i)])	
	print new
	print new_vals		

decompress_vector(d)