class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = 0
        streak = 0
        map = {}

        for c in s:
            if c in map:
                map = {}
                streak = 0

            map[c] = 1
            streak += 1
            longest_string = max(longest_string, streak)

        return longest_string