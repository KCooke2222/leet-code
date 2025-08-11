class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0

        steps = 0
        while r < len(nums) - 1:
            far = r
            for i in range(l, r + 1):
                far = max(far, i + nums[i])
            
            l = r + 1
            r = far
            steps += 1

        return steps

            