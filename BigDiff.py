def big_diff(nums):
	lar=nums[0]
	sm=nums[0]
	for i in nums:
		if i<sm: sm=i
		if i>lar: lar=i
	return lar-sm