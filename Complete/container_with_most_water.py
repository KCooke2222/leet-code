class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        # size of of container is (r - l) * min of l and r vals
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > max_area:
                max_area = area

        
            if heights[l] > heights[r]:
                r -= 1
            else:   # if equal don't matter
                l += 1

        return max_area

