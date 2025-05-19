class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using two pointer method
        l = 0
        r = len(nums) - 1

        while nums[l] + nums[r] != target:
            if nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

        return [l+1, r+1]