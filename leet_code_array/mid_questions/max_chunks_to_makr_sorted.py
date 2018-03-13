class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans=0
        ma=0
        for index, num in enumerate(arr):
            ma= max(ma, num)
            if ma == index:
                ans += 1
        return ans
                
