# swap a pair of first nodes
# recursively swap the remaining and attach it to the second node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        recursive_next_head = head.next.next
        
        node = head
        head = node.next
        head.next = node
        node.next = self.swapPairs(recursive_next_head)
        return head
        
        