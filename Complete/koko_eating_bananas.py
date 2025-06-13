class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_banana(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            return time

        min_k = 1
        max_k = max(piles)

        min_size = max(piles)
        i = 0
        while min_k <= max_k:
            i = (min_k + max_k) // 2
                
            if check_banana(i) > h:
                min_k = i + 1
            else:
                max_k = i - 1
                min_size = min(min_size, i)

        return min_size  
