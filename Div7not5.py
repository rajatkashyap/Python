l=range(2000,3201)
nums=[]
for i in l:
	if i%7==0 and i%5!=0:
		nums.append(str(i))
	
print ','.join(nums)