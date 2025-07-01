class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # kth largest - sorted min to max

        def quickSelect(l, r):
            pivot, p = nums[r], l
            # iterate and get smaller partition
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # swap pivot in middle
            nums[p], nums[r] = nums[r], nums[p]

            # go left, right, or end
            if p > k: 
                return quickSelect(l, p-1)
            elif p < k: 
                return quickSelect(p, r)
            elif p == k: 
                return nums[p]

        return quickSelect(0, len(nums) - 1)