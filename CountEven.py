def count_evens(nums):
	num=0
	for i in nums:
		if i%2==0:
			num+=1
	return num

print count_evens([2, 1, 2, 3, 4])
print count_evens([2, 2, 0])
print count_evens([1, 3, 5])	