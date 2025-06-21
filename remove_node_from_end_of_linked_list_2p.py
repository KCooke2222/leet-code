# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy
        dummy = ListNode()
        dummy.next = head

        # iterate l and r pointer
        l = dummy
        r = head

        for i in range(n):
            r = r.next

        while r: # shift right until it reaches null ptr
            l = l.next
            r = r.next

        # remove node
        l.next = l.next.next

        return dummy.next