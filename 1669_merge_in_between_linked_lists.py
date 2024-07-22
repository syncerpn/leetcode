# fairly easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        na = list1
        i = 0
        while i+1 != a:
            na = na.next
            i += 1
        
        j = i
        nb = na
        while j-1 != b:
            nb = nb.next
            j += 1
        
        na.next = list2
        while na.next:
            na = na.next
        na.next = nb
        return list1

        