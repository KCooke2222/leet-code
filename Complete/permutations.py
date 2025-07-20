class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(cur, nums, selected):
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for i in range(len(nums)):
                if not selected[i]:
                    selected[i] = True
                    cur.append(nums[i])
                    rec(cur, nums, selected)
                    cur.pop()
                    selected[i] = False

        rec([], nums, [False] * len(nums))

        return res