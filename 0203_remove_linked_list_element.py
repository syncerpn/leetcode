#1. track valid node and append it with next valid node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    valid_head = None
    valid_node = None
    node = head
    while node:
        if node.val != val:
            if not valid_head:
                valid_head = node
                valid_node = valid_head
            else:
                valid_node.next = node
                valid_node = node

        node = node.next
        
    if valid_node:
        valid_node.next = None
    return valid_head