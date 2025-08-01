class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_single(arr):
            rob1, rob2 = 0, 0

            for num in arr:
                cur = max(rob2, num + rob1)
                rob1 = rob2
                rob2 = cur

            return rob2

        return max(rob_single(nums[:-1]), rob_single(nums[1:]))
