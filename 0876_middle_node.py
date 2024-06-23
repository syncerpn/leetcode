# its about space or time
# this one sacrifice space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref = []
        while head:
            ref.append(head)
            head = head.next
        
        return ref[len(ref)//2]