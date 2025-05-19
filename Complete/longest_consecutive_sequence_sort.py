class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        # if empty
        if len(nums) == 0:
            return 0

        longest = 1
        current = 1

        # count and change longest 
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i+1] - nums[i] == 1:
                current += 1

                if current > longest:
                    longest = current
            else:
                current = 1

        return longest