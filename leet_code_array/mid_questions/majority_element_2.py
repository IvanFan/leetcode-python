#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1 =0 
        count2 =0
        cand1 =0
        cand2=1
        for x, n in enumerate(nums):
            if n == cand1:
                count1 +=1
            elif n == cand2:
                count2 +=2
            elif count1 == 0:
                cand1 = n
                count1 +=1
            elif count2 == 0:
                cand2 =n
                count2 +=1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (cand1, cand2) if nums.count(n) > len(nums)/3]
