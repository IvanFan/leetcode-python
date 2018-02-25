class ReshapeTheMatrix:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums) * len(nums[0]) != r*c:
            return nums
        one_array = [y for x in nums for y in x]
        result = []
        for x in range(r):
            result.append(one_array[(x*c):((x+1)*c)])
        return result


