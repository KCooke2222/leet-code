class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1

        res = []
        while num != 0:
            res.append(num % 10)
            num //= 10
        
        res.reverse()
        return res