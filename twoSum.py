# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:58:47 2019

@author: u40mv02
"""


def twoSum(nums, target):
    l=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j])==9:
                l.append(i)
                l.append(j)
                break
    return l

print twoSum([13, 17, 6, 3],9)