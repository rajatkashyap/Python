d= {}
x_______1 = [0,1,2,3,4,5,6,7]
d['inds'] = [0,   3,   7,   3,   3,   5, 1]
d['vals'] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
x_true = [1.0, 7.0, 0.0, 11.0, 0.0, 6.0, 0.0, 3.0]
#print d

ind=[]
val=[]
d1={}
for i in d['inds']:
	if i not in ind:
		print i
		print float(d['vals'][d['inds'].index(i)])
		val.append(float(d['vals'][d['inds'].index(i)]))
	else:
		print "ELSE"
		print i
		print float(d['vals'][d['inds'].index(i)]) + val[val.index(i)]
		val.append(float(d['vals'][d['inds'].index(i)]) + val[val.index(i)])

#print ind
#print val




def decompress_vector(d, n=None):
	l=[]
	for (a,b) in zip(d['inds'],d['vals']):
		l.append((a,b))

	return [sum(x) for x in l]

#print decompress_vector(d)