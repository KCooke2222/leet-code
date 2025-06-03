class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        rain = 0
        l_max, r_max = height[l], height[r]

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                rain += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                rain += r_max - height[r]

        return rain


