class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            max_n = nums[i]
            for j in range(k-1):
                max_n = max(max_n, nums[i + j + 1])
            
            res.append(max_n)

        return res