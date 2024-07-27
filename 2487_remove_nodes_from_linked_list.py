# reverse linked list, then make it mono inc and reverse back at the same time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, p = head, None
        while n:
            n.next, p, n = p, n, n.next
        
        n, p = p, None
        while n:
            if p is None or n.val >= p.val:
                n.next, p, n = p, n, n.next
            else:
                n = n.next
        return p