class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_h = []
        for p in points:
            d = math.sqrt(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(min_h, (d,p))

        closest = []
        for i in range(k):
            closest.append(heapq.heappop(min_h)[1])

        return closest