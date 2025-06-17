class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find rotation - last problem (find min value)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid 
        
        min_index = l

        # now we binary search either larger or smaller sub-sorted-arr
        if target <= nums[-1]:
            l, r = min_index, len(nums) - 1
        else:
            l, r = 0, min_index - 1

        # binary search
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1