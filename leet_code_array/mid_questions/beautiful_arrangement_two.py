class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        e.g.
        n=5 k=3

        r:     1  5  2  3  4
        d:      4  3  1  1
        dd:      2    1
        """
        l = 1
        r = n
        result = []
        for x in range(1,n+1):
            if k > 1:
                if k % 2 != 0:
                    result.append(l)
                    l += 1
                elif k % 2 == 0:
                    result.append(r)
                    r -= 1
                k -=1
            else:
                result.append(l)
                l += 1
        return result
