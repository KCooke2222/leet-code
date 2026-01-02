class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # need to get one subset equal to half of the sum
        # track calcuable numbers until the half sum is reached, as long as not above half sum

        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) / 2

        prev_sums = set()
        prev_sums.add(0) # to get the nums itself each time as well
        
        for num in nums:
            new_sums = set()
            for prev_sum in prev_sums:
                new_sum = num + prev_sum
                if new_sum == target:
                    return True
                elif new_sum < target:
                    new_sums.add(new_sum)

            prev_sums.update(new_sums)

        return False





        