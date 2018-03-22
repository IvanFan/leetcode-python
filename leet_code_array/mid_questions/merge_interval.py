#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res=[]
        if len(intervals) == 0:
            return res
        intervals = sorted(intervals, key=lambda interval: interval.start)
        start =intervals[0].start
        end =intervals[0].end
        for i, interval in enumerate(intervals):
            if interval.start <= end:
                start = min(start, interval.start)
                end = max(end, interval.end)
            else:
                res.append(Interval(start, end))
                start = interval.start
                end = interval.end
        res.append(Interval(start, end))
        return res
