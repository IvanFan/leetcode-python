#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def binarySearch(self, nums, target, l, r):
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return mid
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        lindex = self.binarySearch(nums, target, 0, r-1)
        rindex = self.binarySearch(nums, target, r, len(nums)-1)
        return max(lindex,rindex)




