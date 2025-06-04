class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = {}
        maj = 0 # majority char (to get minority take total - maj)
        l = 0 

        for r in range(len(s)):
            # add char
            chars[s[r]] = chars.get(s[r], 0) + 1

            # update majority char
            maj = max(maj, chars[s[r]])

            # check if minority > k
            while (r-l+1) - maj  > k:
                chars[s[l]] -= 1
                l += 1

            # get result
            res = max(res, r-l+1)

        return res
            