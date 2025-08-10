class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in memo:
                return memo[i, total]

            # sub
            sub = dfs(i + 1, total - nums[i])

            # add
            add = dfs(i + 1, total + nums[i])

            memo[(i, total)] = sub + add

            return memo[(i, total)]

        return dfs(0, 0)