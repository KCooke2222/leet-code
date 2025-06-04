class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = 0
        l, r = 0, 0
        dup = set()

        while r < len(s):
            # if right most is in dup (duplicate), shift left
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
                
            # add right to dup
            dup.add(s[r])

            # check length
            if r-l+1 > longest_string:
                longest_string = r-l+1

            # move right 
            r += 1


        return longest_string