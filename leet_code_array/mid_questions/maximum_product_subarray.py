#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxpre = nums[0]
        minpre = nums[0]
        maxnow = maxpre
        minnow = minpre
        maxsofar = nums[0]
        nl = len(nums)
        for x in range(1,nl):
            maxnow = max(max(minpre*nums[x], maxpre* nums[x]), nums[x])
            minnow = min(min(minpre*nums[x], maxpre*nums[x]), nums[x])
            maxsofar = max(maxnow, maxsofar)
            maxpre = maxnow
            minpre = minnow
        return maxsofar
