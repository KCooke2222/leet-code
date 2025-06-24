# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def dfs(root):
            if not root:
                return 0

            height_l = dfs(root.left)
            height_r = dfs(root.right)

            self.d = max(self.d, height_l + height_r)  

            return max(height_r, height_l) + 1

        dfs(root)

        return self.d
        