#1. swap a pair of first nodes
#2. recursively swap the remaining and attach it to the second node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    if head is None:
        return None
    if head.next is None:
        return head
    
    recursive_next_head = head.next.next
    
    node = head
    head = node.next
    head.next = node
    node.next = swapPairs(recursive_next_head)
    return head
