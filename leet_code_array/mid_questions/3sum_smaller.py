#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            if nums[i] * 3 >= target:
                return count
            start = i+1
            end= len(nums)-1
            while start < end:
                if nums[i] + nums[start] + nums[end] < target:
                    count += end - start
                    start += 1
                else:
                    end -= 1
        return count
                
        
