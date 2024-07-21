# insert is easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        p = head
        n = head.next
        while n:
            a = ListNode(gcd(p.val, n.val), next=n)
            p.next = a
            p, n = n, n.next
        return head
