"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # first pass copy and create hash
        nodes = {}

        node = head
        prev_node = Node(node.val)
        new_head = prev_node

        nodes[node] = prev_node

        node = node.next

        while node:
            next_node = Node(node.val)
            prev_node.next = next_node

            nodes[node] = next_node

            prev_node = next_node
            node = node.next

        # second pass assign random pointers on copy
        l1 = head
        l2 = new_head

        while l1:
            if l1.random:
                l2.random = nodes[l1.random]

            l1 = l1.next
            l2 = l2.next

        return new_head