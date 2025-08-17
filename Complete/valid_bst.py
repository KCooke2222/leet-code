# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        ok = True

        def inorder(node):
            nonlocal prev, ok
            if not node or not ok:
                return

            inorder(node.left)
            if node.val <= prev:
                ok = False
                return
            prev = node.val
            inorder(node.right)

        inorder(root)
        return ok