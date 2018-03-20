#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res= [[0]*n for x in range(n)]
        count = 1
        r=c=di=0
        dr= [0,1,0,-1]
        dc= [1,0,-1,0]
        for _ in range(n*n):
            res[r][c]=count
            count+=1
            rn,cn=r+dr[di],c+dc[di]
            if 0<=rn<n and 0<=cn<n and res[rn][cn] == 0:
                r,c = rn,cn
            else:
                di = di+1%4
                r,c=r+dr[di],c+dc[di]
        return res
