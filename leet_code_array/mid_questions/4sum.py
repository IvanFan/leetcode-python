#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def threeSum(self, nums, target, ans,index, previous, lnum):
        for i in range(index, lnum-2):
            if (3 * nums[i]) > target:
                return
            if (3*nums[lnum-1])<target:
                return
            if i > index and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = lnum -1
            while l < r:
                cursum = nums[i] + nums[l] + nums[r]
                if cursum == target:
                    ans.append([previous, nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l = l+1
                    while l < r and nums[r] == nums[r-1]:
                        r =r-1
                    l = l+1
                    r= r-1
                elif cursum < target:
                    l +=1
                else:
                    r-=1
        return


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        lnum = len(nums)
        if lnum <4:
            return ans
        if nums[0]*4 > target:
            return ans
        if nums[lnum-1] * 4 < target:
            return ans
        for i in range(lnum-3):
            if (nums[i] + 3*nums[lnum-1]) < target:
                continue
            if (nums[i]+ 3*nums[i+1]) > target:
                continue
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4 == target:
                if i+3 < lnum and nums[i] == nums[i+3]:
                    ans.append([nums[i]]*4)
                    continue
            self.threeSum(nums, target - nums[i], ans, i+1, nums[i], lnum)

        return ans
