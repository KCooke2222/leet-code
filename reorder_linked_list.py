# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find center
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev, curr = None, slow.next
        slow.next = None  # cut first half

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # build alternating between each half
        l1 = head
        l2 = prev

        l1, l2 = head, prev
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            if not tmp1:
                break
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2

        # prevent cycle
        if l2:
            l2.next = None


