#1. two nodes, each starts at the head of each linked list
#2. make sure they travel the same trackable distance, which equals to unique A nodes + unique B nodes + common nodes
#3. they travel all unique nodes of their head, then common nodes, then unique nodes of the opponent
#4. they will meet at the intersection node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solve(headA: ListNode, headB: ListNode) -> ListNode:
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