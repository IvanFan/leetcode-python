#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        nl = len(nums)
        if nl ==0:
            return res
        start = nums[0]
        end = nums[0]
        for x in range(1,nl):
            if nums[x] == end + 1:
                end = nums[x]
            else:
                res.append(start,'=>',end)
                start = nums[x]
                end = nums[x]
        return res

