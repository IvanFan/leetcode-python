#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cand = 0
        mindis = 9999
        nl = len(nums)
        if nl == 3:
            return sum(nums)
        nums.sort()
        for x in range(nl-2):
            print('x:',x)
            l = x+1
            r = nl -1
            curmax = nums[x] + nums[r] + nums[r-1]
            print('curmax:', curmax)
            curmin = nums[x] + nums[l] + nums[l+1]
            print('curmin:', curmin)
            print('dis max', abs(target - curmax))
            print('dis min', abs(target - curmin))
            print('mindis', mindis)
            if curmax  < target:
                if mindis > abs(target - curmax):
                    mindis = abs(target - curmax)
                    cand = curmax
                continue
            if curmin > target:
                if mindis > abs(target - curmin):
                    mindis = abs(target - curmin)
                    cand = curmin
                continue
            while l < r:
                cursum = nums[x] + nums[l] + nums[r]
                print('x:',x,'l:',l,'r:',r, 'sum:',cursum)
                if abs(target - cursum) < mindis:
                    mindis =abs(target - cursum)
                    cand = cursum
                if cursum < target:
                    l += 1
                elif cursum > target:
                    r -= 1
                elif cursum == target:
                    return cursum
        return cand
