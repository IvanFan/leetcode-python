class Solution:
    def backTrace(self, candidates, index, curList, remain, res):
        if remain == 0:
            res.append(curList)
            return
        elif remain < 0:
            return
        else:
            for x in range(index, len(candidates)):
                self.backTrace(candidates, x, curList + [candidates[x]], remain-candidates[x], res)
        

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.backTrace(candidates, 0, [], target, res)
        return res
