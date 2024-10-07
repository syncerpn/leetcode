# two-pass
# count first, then modify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n, prev, node = 0, None, head
        while node:
            prev, node = node, node.next
            n += 1
        
        tail = prev
        k = k % n
        if k == 0:
            return head
        i, node = 0, head
        for _ in range(n-k):
            prev = node
            node = node.next
        
        prev.next = None
        tail.next = head
        return node


# without counting the list seems also possible
# but maybe not worth it because k maybe even larger than n
# and in such case, moving with fast-slow approach is more expensive than just counting it