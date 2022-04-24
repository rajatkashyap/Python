def checkio1(list):
	return [x for x in list if list.count(x)>1]
	

def checkio2(list):
	list_count=[]
	for i in list:
		if list.count(i)>1:
			list_count.append(i)
	
	return list_count
		
def checkio3(list):
	dict_count={}
	list_count=[]
	for i in list:
		dict_count[i]=list.count(i)
	
	for i in list:
		if dict_count[i]>1:
			list_count.append(i)
	return list_count

def checkio(list):	
    new=[]
    new_d={}
    for i in list:
        if i not in new_d:
            new_d[i]=list.count(i)
    print new_d
    
    for i in list:
        if new_d[i]>1:
            new.append(i)
    
    return new

print checkio([10, 9, 10, 10, 9, 8, 6, 7, 7])
