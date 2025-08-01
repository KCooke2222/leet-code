class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one = cost[n - 1]
        two = 0

        for step in range(n - 2, -1, -1):
            step = cost[step] + min(one, two)

            two = one
            one = step

        return min(one, two)