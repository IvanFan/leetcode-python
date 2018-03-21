#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for x in range(len(nums)-2):
            if nums[x] > 0:
                break
            if x > 0 and nums[x] == nums[x-1]:
                continue
            y = x+1
            z = len(nums) -1
            while y < z:
                cursum = nums[x] + nums[y] + nums[z]
                if cursum == 0:
                    ans.append([nums[x],nums[y],nums[z]])
                    while y<z and nums[y] == nums[y+1]:
                        y+= 1
                    while y<z and nums[z] == nums[z-1]:
                        z-=1
                    y+=1
                    z-=1
                elif cursum <0:
                    y += 1
                else:
                    z -= 1
        return ans

