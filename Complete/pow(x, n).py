class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        og = n # store sign
        n = abs(n)
        while n != 0:
            if n % 2:
                res *= x
            
            x *= x
            n >>= 1

        if og < 0:
            res = 1/ res
        
        return res