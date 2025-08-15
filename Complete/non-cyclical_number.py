class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            n2 = 0
            for ch in str(n):
                n2 += int(ch) ** 2
            n = n2

        return True