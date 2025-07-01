class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we use a max heap (negative values)
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # get heavy stones
            x = -(heapq.heappop(stones))
            y = -(heapq.heappop(stones))

            # get ending weight
            if abs(x - y):
                heapq.heappush(stones, -abs(x-y))

        return -stones[0] if stones else 0