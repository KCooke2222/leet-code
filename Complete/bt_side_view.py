# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        def bfs(root):
            q = deque([root])

            while q:
                level_size = len(q)

                r_node = 0
                for node in range(level_size):
                    node = q.popleft()
                    r_node = node

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                res.append(r_node.val)

        bfs(root)

        return res
