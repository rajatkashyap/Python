'''def sum67(nums):
	if 6 in nums and 7 in nums and nums.index(6)<nums.index(7):
		print nums[:nums.index(6)]
		print nums[nums.index(7)+1:]
		nums2=nums[:nums.index(6)]+nums[nums.index(7)+1:]
		print nums2
	else: nums2=nums
	if nums2==[]: return 0
	else: return sum(nums2)

	
def sum67(nums):
total=0
	for i in range(len(nums)):
			if 6 in nums and 7 in nums and nums.index(6)<nums.index(7):
				total=total+sum(nums[:nums.index(6)]+nums[nums.index(7)+1:])
'''

def sum67(nums):
	nums1=[]
	for i in nums:
		if i!=6:
			nums1.append(i)
		else:
			if i==6:
				for x in range(nums.index(6)
					
	
	
	
print (sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
