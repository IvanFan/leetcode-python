#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = []
        c = []
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    r.append(x)
                    c.append(y)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in r or y in c:
                    matrix[x][y] = 0
        
