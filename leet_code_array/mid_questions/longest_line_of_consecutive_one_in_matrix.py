#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def longestLine(self, M):
        if len(M) == 0:
            return 0
        rows, columns = len(M), len(M[0])
        maxcount = 0
        dp = [ [[[0]*4 for c in range(columns)]] for r in range(rows)]
        for r in range(rows):
            for c in range(columns):
                if M[r][c] == 1:
                    dp[r][c][0] = dp[r][c-1][0] +1 if c > 0 else 1
                    dp[r][c][1] = dp[r-1][c][1] + 1 if r > 0 else 1
                    dp[r][c][2] = dp[r-1][c+1][2] +1 if r > 0 and c < columns -1 else 1
                    dp[r][c][3] = dp[r-1][c-1][3] +1 if r >0 and c>0 else 1
                    maxcount = max(maxcount,max(dp[r][c]))
        return maxcount

