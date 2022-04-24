d= {}
d['inds'] = [0,   3,   7,   3,   3,   5, 1]
d['vals'] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
x_true = [1.0, 7.0, 0.0, 11.0, 0.0, 6.0, 0.0, 3.0]
print d

def decompress_vector(d, n=None):
	lt=[]
	if n is None: 
		l=max(d['inds'])+1
	else:
		l=n
	for i in range(len(d['inds'])):
		lt.append((d['inds'][i],d['vals'][i]))

	print l
	print lt
	lt1=[]
	for i in range(l):
		for j in range(i+1,l):
			if lt[i][0]==lt[j][0]:
				lt[1].append(lt[i][0],lt[i][1]+lt[j][1])
				





decompress_vector(d)
		
