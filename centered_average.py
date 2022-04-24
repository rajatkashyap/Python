'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
'''
def centered_average(nums):
	s=nums[0]
	l=nums[0]
	nums1=[]
	for i in nums:
		if i<s: s=i
		if i>l: l=i
	print s
	print l
	for i in nums:
		if i==s or i==l:
			if nums.count(i)>1 and i not in nums1:
				print 'yes'
				nums1.append(i)
		else:
			print 'added again'
			nums1.append(i)
	return sum(nums1)/len(nums1)

print centered_average([1,2, 3, 4, 100])			
	