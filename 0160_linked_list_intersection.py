# two nodes, each starts at the head of each linked list
# make sure they travel the same trackable distance, which equals to unique A nodes + unique B nodes + common nodes
# they travel all unique nodes of their head, then common nodes, then unique nodes of the opponent
# they will meet at the intersection node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b:
            if not a:
                a = headB
            else:
                a = a.next
            
            if not b:
                b = headA
            else:
                b = b.next
        
        return a