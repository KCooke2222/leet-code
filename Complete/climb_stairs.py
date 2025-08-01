class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for step in range (n - 3, 0, -1):
            step = one + two

            two = one
            one = step

        return one
