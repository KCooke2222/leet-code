class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recursive(comb, sums, nums):
            if sums == target:
                res.append(comb)
                return

            # if can add add
            # but if not must purge all of the num going down other path
            if nums and (sums + nums[0]) <= target:
                recursive(comb + [nums[0]], sums + nums[0], nums[1:])
            if nums:
                i = 1
                while i < len(nums) and nums[i] == nums[0]:
                        i +=1
                recursive(comb, sums, nums[i:])

        nums.sort()
        recursive([], 0, nums)

        return res