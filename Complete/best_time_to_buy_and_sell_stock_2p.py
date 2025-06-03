class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Same as dp solution but using pointers
        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                max_p = max(max_p, prices[r] - prices[l])
            else:
                l = r

            r += 1

        return max_p
