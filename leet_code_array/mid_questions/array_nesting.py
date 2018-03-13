class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums
        maxLength=0
        for index, num in enumerate(nums):
            if num >= 0:
                curCircleLength = 1
                temp = nums[index]
                nums[index] = -1
                while nums[temp] >= 0:
                    previous=temp
                    temp = nums[previous]
                    curCircleLength += 1
                    nums[previous] = -1
                maxLength=max(curCircleLength, maxLength)
        return maxLength


        