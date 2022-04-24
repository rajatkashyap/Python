
'''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) → 2	
sum67([2, 7, 6, 2, 6, 2, 7]) → 9	
'''

'''def sum67(nums):
  if 6 not in nums:
    return sum(nums)
  else:
      if 7 not in nums:
          return sum(nums)   
    
  i=nums.index(6)
  j=nums.index(7)
  newarr=nums[:i]+nums[j+1:]
  return sum(newarr)
'''
def sum67(nums):
    newarr=[]
    if 6 not in nums:
        return sum(nums)
    else:
        if 7 not in nums:
            return sum(nums)  
      

    for i in nums:
        if i!=6:
            newarr.append(i)
        else:
            i_6=nums.index(i)
            i_7=nums[i_6:].index(7)
    

   
print sum67([1, 2, 2, 6, 99, 99, 7,7])
print sum67([1, 2, 2])
print sum67([1, 2, 2,6,8,9])