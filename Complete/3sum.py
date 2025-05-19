class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # solve - slow b/c do checking at end to filter results
        # does permuataion strat (5*4*3...)
        for i in nums:
            nums2 = nums.copy()
            nums2.remove(i)
            for j in nums2:
                nums3 = nums2.copy()
                nums3.remove(j)
                for k in nums3:
                    if i + j + k == 0:
                        triplet = sorted([i, j, k])
                        if triplet not in result:
                            result.append(triplet)

        return result