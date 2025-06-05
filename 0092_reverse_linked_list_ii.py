# it is 1-index position, lol
# anyway, easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        r = head
        l, m, t = None, None, None
        for i in range(right):
            if i + 1 < left:
                if l:
                    l.next = r
                l = r
                r = r.next
            else:
                if not t:
                    t = r
                k = r.next
                r.next = m
                m = r
                r = k
        
        t.next = r
        if l:
            l.next = m
            return head
        return m
