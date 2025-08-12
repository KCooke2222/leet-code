"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=lambda x: x.start)

        prev_end = intervals[0].end

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end

            if start < prev_end:
                return False
            else:
                prev_end = end

        return True