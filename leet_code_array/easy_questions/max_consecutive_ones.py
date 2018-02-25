class MaxConsecutiveOnes:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max = count if max < count else max
                count = 0
        return count if max < count else max