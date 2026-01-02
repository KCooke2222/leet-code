"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s = 0
        e = 0

        res = 0
        overlap = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                overlap += 1
                res = max(res, overlap)
                s += 1
            else:
                overlap -= 1
                e += 1
        
        return res
