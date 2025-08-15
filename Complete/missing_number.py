class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            res ^= nums[i] ^ i
        
        res ^= n

        return res

        