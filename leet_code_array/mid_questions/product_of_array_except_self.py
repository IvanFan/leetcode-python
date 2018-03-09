class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        fromStart = 1
        fromEnd = 1
        n=len(nums)
        res = [1] * n
        for index, num in enumerate(nums):
            res[index] *= fromStart
            fromStart *=nums[index]
            res[n-1-index]*=fromEnd
            fromEnd*=nums[n-1-index]
        return res