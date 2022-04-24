# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:11:46 2019
'[-1, 0, 1, 2, -1, -4]
'[-4, -1, -1, 0, 1, 2]
@author: u40mv02
"""


def threeSum(nums):
    z=len(nums)-1
    res=[]
    nums.sort()
    for x in range(len(nums)-2):
        y=x+1
        while(y<z):
            s=nums[x]+nums[y]+nums[z]
            if s<0:
                y=y+1
            if s>0:
                z=z-1
            if s==0:
                if [nums[x],nums[y],nums[z]] not in res:
                    res.append([nums[x],nums[y],nums[z]])
                x+=1
    return res


print threeSum([-1, 0, 1, 2, -1, -4,1,5])        
    
       