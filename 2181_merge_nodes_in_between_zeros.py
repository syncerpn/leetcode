# pretty simple though
# just traversal
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head.next
        n = head.next.next
        while n:
            if n.val != 0:
                p.val += n.val
            else:
                n = n.next
                p.next = n
                p = n
            if n:
                n = n.next
        return head.next