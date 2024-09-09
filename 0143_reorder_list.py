# reverse the second part
# then merge them
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
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
        
        f, s = head, head
        while f:
            f = f.next
            if not f:
                break
            f = f.next
            s = s.next
        f = head
        s = reverseList(s)
        while s:
            t = f.next
            f.next = s
            f = s
            s = t
        f.next = None
        return head