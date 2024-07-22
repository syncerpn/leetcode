# hare and turquoise mechanism to find mid of the even-length linked list
# then stack pop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        h = head
        t = head.next
        s = [h.val]
        while t.next:
            h = h.next
            s.append(h.val)
            t = t.next.next
            
        m = 0
        while h.next:
            h = h.next
            m = max(m, h.val + s.pop())
        return m