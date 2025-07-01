class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        # pop until kth
        for i in range(k):
            res = heapq.heappop(nums)

        return -res