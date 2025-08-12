class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort first
        intervals.sort(key=lambda x: x[0])
        
        res = []
        start, end = intervals[0]


        for i in range(len(intervals) - 1):
            # push non-overlap intervals
            if intervals[i+1][0] > end:
                res.append([start, end])
                start, end = intervals[i+1]

            # adjust merge
            else:
                start = min(start, intervals[i+1][0])
                end = max(end, intervals[i+1][1])

        res.append([start, end])
        return res
