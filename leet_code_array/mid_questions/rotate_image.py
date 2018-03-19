#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        for r in range(rows):
            for c in range(r+1, rows):
                temp = matrix[c][r]
                temp2 =  matrix[r][c]
                matrix[c][r] = temp2
                matrix[r][c] = temp
        for r in range(rows):
             matrix[r] = list(reversed(matrix[r]))
        
