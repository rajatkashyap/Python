example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5,4,3,2]

example_list.sort()

print(example_list)
y=len(example_list)
print(y)
if y%2==0:
	print (example_list[y//2]-1+example_list[y//2])/2.0
else:
	print example_list[y//2]

sum=0
for items in   example_list:
    sum+=items

m=(sum/y)*1.00
print "Mean: %.2f" %m
print "Mean: ", m