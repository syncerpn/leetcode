# use stack for a simple solution
# too lazy to implement a better one
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        s = []
        while node:
            s.append(node.val)
            node = node.next

        c = 0
        q = None
        while s:
            v = s.pop()
            v = v * 2 + c
            if v > 9:
                c = 1
                v -= 10
            else:
                c = 0
            q = ListNode(v, q)
        
        if c == 1:
            q = ListNode(c, q)
        return q