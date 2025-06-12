class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1

        while min <= max:
            i = (min + max) // 2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                max = i - 1
            else:
                min = i + 1

        return -1  # target not found