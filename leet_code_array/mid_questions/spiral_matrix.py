class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        rnum=len(matrix)
        if rnum == 0:
            return 0
        cnum=len(matrix[0])
        if cnum == 0:
            return 0

        seen= [[False] * cnum for x in range(rnum)]
        dr= [0, 1, 0, -1]
        dc= [1, 0, -1, 0]
        r=c=di = 0
        for _ in range(rnum * cnum):
            ans.append(matrix[r][c])
            seen[r][c] = True
            rnext,cnext = r + dr[di],c+dc[di]
            if rnext >= 0 and rnext<rnum and cnext >= 0 and cnext < cnum and not seen[rnext][cnext]:
                r,c = rnext,cnext
            else:
                di = (di +1) %4
                r,c = r + dr[di],c+dc[di]
        return ans
