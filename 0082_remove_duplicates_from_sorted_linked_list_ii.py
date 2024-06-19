# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy_head = ListNode(val=None, next=head)
        node_pp = dummy_head
        node_p = head
        node = head.next
        while node:
            # using the fact that input linked list is sorted, switching node only when this is true
            if node_pp.next.val < node_p.val:
                node_pp = node_pp.next
            if node.val == node_p.val:
                node_pp.next = node.next
            node_p = node
            node = node.next

        return dummy_head.next