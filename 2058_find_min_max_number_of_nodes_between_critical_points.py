# fairly simple though
# just traversal and keep track of first and last critical points
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = None
        last = None
        
        p = head
        c = head.next
        n = head.next.next
        
        i = 1
        d_min = -1
        d_max = -1

        while n:
            if (c.val > p.val and c.val > n.val) or (c.val < p.val and c.val < n.val):
                if first is None:
                    first = i
                    last = i
                else:
                    d_min = min(d_min, i - last) if d_min != -1 else i - last
                    last = i
                    d_max = last - first

                
            p, c, n = c, n, n.next
            i += 1
        
        return [d_min, d_max]