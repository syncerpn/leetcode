# easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l, r = None, None
        lh, rh = None, None
        n = head
        while n:
            if n.val < x:
                if l:
                    l.next = n
                else:
                    lh = n
                l = n
            else:
                if r:
                    r.next = n
                else:
                    rh = n
                r = n
            
            n = n.next
        
        if rh:
            r.next = None
            
        if lh:
            l.next = rh
            return lh
        return rh