class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        letterList = [0]*26
        for letter in tasks:
            letterList[string.ascii_uppercase.index(letter)] += 1
        
        maxValue = max(letterList) - 1
        print(maxValue)
        idealSlot = maxValue * (n+1)
        print(idealSlot)
        for index, letterSum in enumerate(letterList):
            idealSlot -= min(letterSum, maxValue)
        if idealSlot > 0: 
            return idealSlot + len(tasks)
        else: 
            return len(tasks)
        