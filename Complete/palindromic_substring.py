class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for c in range(len(s)):
            # one center ---
            i = c
            j = c

            # expand palindrom outwards
            while i >= 0 and j <= len(s) - 1:
                if s[i] != s[j]:
                    break
                
                res += 1

                i -= 1
                j += 1


            # two center ---
            i = c
            j = c + 1

            # expand palindrom outwards
            while i >= 0 and j <= len(s) - 1:
                if s[i] != s[j]:
                    break

                res += 1

                i -= 1
                j += 1

        return res