class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur)
                return

            if i >= len(nums) or total > target:
                return
            
            dfs(i+1, cur + [nums[i]], total + nums[i])

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1

            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res