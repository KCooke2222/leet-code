class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = []
        prefix = [1] * n
        suffix = [1] * n

        # build prefix
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # build suffix
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # mult each
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result