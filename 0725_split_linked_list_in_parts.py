# two-pass
# one to count
# one to split
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, node = 0, head
        while node:
            n += 1
            node = node.next
        
        q, r = n // k, n % k
        s, ans = [q + 1] * r + [q] * (k - r), [head]
        node = head
        for si in s[:-1]:
            for i in range(si):
                nn = node.next
                if i == si-1:
                    node.next = None
                node = nn
            ans.append(node)
        return ans