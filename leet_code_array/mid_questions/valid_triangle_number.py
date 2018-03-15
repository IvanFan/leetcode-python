#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    """
    one solution backtracking 
    """
    def __init__(self):
        self.result = 0
        
    def testIfMatch(self, res):
        t1= res[0]+res[1]-res[2]
        t2= res[1]+res[2]-res[0]
        t3=res[0]+res[2]-res[1]

        z1= res[0]-res[1]-res[2]
        z2= res[1]-res[2]-res[0]
        z3=res[0]-res[2]-res[1]
        if t1 >0 and t2 >0 and t3>0 and z1<0and z2<0 and z3<0:
            self.result += 1


    def backTrace(self, index, nums, res):
        if len(res) == 3:
            self.testIfMatch(res)
            return True
        if index == len(nums):
            return True
        for t in range(index, len(nums)):
            res.append(nums[t])
            self.backTrace(t+1, nums, res)
            res.pop()


    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for index, num in enumerate(nums):
            res.append(nums[index])
            self.backTrace(index+1, nums, res)
            res.pop()
        return self.result
