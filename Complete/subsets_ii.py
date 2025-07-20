class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            bt(i + 1, subset)
            subset.pop()

            # Skip duplicates in the exclude path
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            bt(i + 1, subset)

        bt(0, [])
        return res