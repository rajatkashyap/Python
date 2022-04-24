def checkio(l):
	l1=[]
	for i in l:
		if l.count(i)>1:
				l1.append(i)
	return l1			
	
	
	'''d={}
	l1=[]
	for x in l:
		d[x]=d.get(x,0)+1
	#print d
	for x in l:
		if d[x]>1:
			l1.append(x)
	return l1	'''
	
	#return [x for x in l if l.count(x)>1]
    
    
def checkio1(l):
    l2=[]
    for i in l:
        if l.count(i)>1:
            l2.append(i)
    return l2


if __name__ == "__main__":
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert isinstance(checkio([1]), list), "The result must be a list"
	assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
	assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
	assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
	assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
	assert isinstance(checkio1([1]), list), "The result must be a list"
	assert checkio1([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
	assert checkio1([1, 2, 3, 4, 5]) == [], "2nd example"
	assert checkio1([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
	assert checkio1([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"