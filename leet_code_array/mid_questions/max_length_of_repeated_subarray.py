#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        hashTable = [[0]* (len(B)+1) for _ in range(len(A)+1)]
        for x in range(len(A)-1, -1, -1):
            for y in range(len(B)-1 , -1, -1):
                if A[x] == B[y]:
                    hashTable[x][y] = hashTable[x][y] + 1
        maxcount = 0
        maxcount = max([max(hashTable[x]) for x in range(len(hashTable))])
        return maxcount

