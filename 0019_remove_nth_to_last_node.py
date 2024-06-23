# create a dummy node to deal with removing head
# save two nodes for reference, they should be away from each other by a distance of n+1
# keep travelling until one reaches the last node
# the other should now be the prev node of the target node
# simple assign its next node to the next of the target node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        prev_to_target_node = dummy
        last_node = dummy

        for _ in range(n+1):
            last_node = last_node.next
        
        while last_node is not None:
            last_node = last_node.next
            prev_to_target_node = prev_to_target_node.next
        
        prev_to_target_node.next = prev_to_target_node.next.next

        return dummy.next