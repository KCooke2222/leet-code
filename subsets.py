class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # exclude
            dfs(i + 1)

            # include
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            

        dfs(0)

        return res