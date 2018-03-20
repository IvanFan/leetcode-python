#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l < r:
            m = l + (r-l)/2
            if nums[l] < nums[m]:
                l = m
            else:
                r = m
        return nums[r]
