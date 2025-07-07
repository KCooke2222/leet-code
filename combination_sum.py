class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recursive(comb, sums, nums):
            if sums == target:
                res.append(comb)
                return

            if nums and (sums + nums[0]) <= target:
                recursive(comb + [nums[0]], sums + nums[0], nums)
            if nums:
                recursive(comb, sums, nums[1:])

        recursive([], 0, nums)

        return res