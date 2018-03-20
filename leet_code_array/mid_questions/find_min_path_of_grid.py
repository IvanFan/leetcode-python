#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def findPath(self, grid):
        r = len(grid)
    c = len(grid[0])
    maxN =sum([sum(grid[x]) for x in range(r)])
    minTable = [[maxN]* c for x in range(r)]
    for x in range(r):
      for y in range(c):
         if x ==0 and y == 0:
            minTable[x][y] = grid[x][y]
         elif x == 0:
            minTable[x][y] = grid[x][y] + minTable[x][y-1]
         elif y == 0:
            minTable[x][y] = grid[x][y] + minTable[x-1][y]
         else:
            minTable[x][y] = min(grid[x][y] + minTable[x-1][y], grid[x][y] + minTable[x][y-1])
    return minTable[r-1][c-1]

