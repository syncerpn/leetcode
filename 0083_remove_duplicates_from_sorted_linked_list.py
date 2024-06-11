#1. keep track of last unique node during traversal
#2. link them together
#3. dont forget to link the last unique node to None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    if not head:
        return head

    node_unique = head
    node = head.next
    while node:
        if node.val != node_unique.val:
            node_unique.next = node
            node_unique = node
        
        node = node.next
        
    node_unique.next = None
    return head