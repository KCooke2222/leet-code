class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bars = [] # i, h
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while bars and bars[-1][1] > h:
                max_area = max(max_area, bars[-1][1] * (i - bars[-1][0]))
                start = bars[-1][0]
                bars.pop()

            bars.append((start,h))

        for i, h in bars:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

