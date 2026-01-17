class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]

        for t in triplets:
            # Check if we can perform operation
            valid = True
            for index, num in enumerate(t):
                if num > target[index]:
                    valid = False
                    break
            
            # perform operation
            if valid:
                for index, num in enumerate(t):
                    res[index] = max(res[index], num)
        
        return res == target

