# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev
            

        # n-1.next = n-1.next.next
        # just del first element
        if n == 1:
            head = head.next  # remove first node
        else:
            n_sub_1 = head
            for i in range(n - 2):
                n_sub_1 = n_sub_1.next

            if n_sub_1 and n_sub_1.next:
                n_sub_1.next = n_sub_1.next.next
            else:
                n_sub_1.next = None  # remove tail


        # reverse
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev