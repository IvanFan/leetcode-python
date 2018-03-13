class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs([], 0, nums, res)
        return res
    
    def dfs(self, path, index, nums, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(path + [nums[i]], i+1, nums, res)