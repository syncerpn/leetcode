# easy as it is
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        d = 0
        while head:
            d = d * 2 + head.val
            head = head.next
        return d

# bitwise op is much faster than above
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        d = 0
        while head:
            d = d << 1 | head.val
            head = head.next
        return d