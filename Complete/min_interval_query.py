class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        # (query_value, original_index)
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [0] * len(queries)
        heap = []
        i = 0
        for q in queries:
            # Collect intervals
            while i < len(intervals) and intervals[i][0] <= q[0]:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (length, intervals[i][1]))
                i += 1

            while heap and heap[0][1] < q[0]:
                heapq.heappop(heap)

            if heap:
                res[q[1]] = heap[0][0]
            else:
                res[q[1]] = -1

        return res