# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, big):
            if not node:
                return 0

            good = 0
            if node.val >= big:
                good = 1
                big = node.val
            
            return good + dfs(node.left, big) + dfs(node.right, big)

        return dfs(root, float('-inf'))