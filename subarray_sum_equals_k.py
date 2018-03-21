#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
        def subarraySum(self, nums, k):
            sumhash = {}
            sumN = 0
            count = 0
            for x in range(len(nums)):
                sumN=sumN + nums[x]
                if (sumN - k) in sumhash:
                    count += sumhash[sumN-k]
                if sumN in sumhash:
                    sumhash[sumN] += 1
                else: 
                    sumhash[sumN] = 1
            return count
