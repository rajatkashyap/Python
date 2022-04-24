list1=['rajat','charu','parag','barkha',1,2,3,7.8,9.0,['delhi','mumbai'],1,1]

list2=[]
list3=[]
for i in list1:
	print "And the name is: %r" %i
'''
	
	
for i in range(0,6):
	x=input("input a no")
	list2.append(x)

	
print list2

for i in range(0,6):
	x=input("input a no")
	list3.append(x)
	
print list2+list3

list4=[]
'''
list4=range(0,4)

print list4
print list1[0]

print list1.count(1)

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print aList

print aList+bList

print len(list1)

list1.append('Moyne')

print list1

if 'rajat1' in list1:
	print "Its there"
else: 
	print "Not There"

s = lambda y: y ** y; print s(3)

