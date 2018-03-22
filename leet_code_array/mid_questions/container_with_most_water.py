#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        cursize = 0
        maxsize = 0
        rl = len(height)
        l = 0
        r = rl -1
        while l < r:
            cursize = abs(r-l) * min(r, l)
            maxsize = max(maxsize, cursize)
            if l < r:
                l += 1
            else:
                r -= 1
        return maxsize
