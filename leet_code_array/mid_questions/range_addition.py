class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result=[0] * length
        for operation in updates:
            result[operation[0]] = result[operation[0]] + operation[2]
            if operation[1] < length - 1:
                result[operation[1] + 1] = result[operation[1] + 1] - operation[2]
        tem = 0
        for index in range(length):
            tem = tem + result[index]
            result[index] = tem
        return result
        