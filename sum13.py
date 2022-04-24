def sum13(nums):
	sum=0
	for i in range(len(nums)):
		print nums[i]
		if nums[i]==13 or (nums[i-1]==13 and i!=0):
			print 'Inside', nums[i]
			continue
		sum+=nums[i]
	print sum  
 
sum13([1, 2, 2, 1, 13,5]) 
  