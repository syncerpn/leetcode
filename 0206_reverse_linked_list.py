# iterate and remember
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        node = head
        node_next = node.next
        node.next = None
        while node_next:
            t = node_next.next
            node_next.next = node
            node = node_next
            node_next = t
        
        return node