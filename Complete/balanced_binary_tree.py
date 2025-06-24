# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root):
            if not root:
                return 0

            height_l = dfs(root.left)
            height_r = dfs(root.right)

            if abs(height_l - height_r) > 1:
                self.res = False 

            return max(height_r, height_l) + 1

        dfs(root)

        return self.res