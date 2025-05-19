class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if j != i:
                    num *= nums[j]
            
            result.append(num)

        return result