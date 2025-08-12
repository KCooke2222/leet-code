class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dist = 0
        for n in reversed(nums):
            if n >= dist:
                dist = 1
            else:
                dist += 1

        return True if dist == 1 else False         

            
