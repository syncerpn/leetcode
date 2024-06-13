#1. reverse second half of the linked list and compare with the first half
#2. this one is not so clean; floyd traversal can be used to improve
#3. for O(N) space solution, just use list and two pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> bool:
    def reverse(head):
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
            
    n = 0
    node = head
    while node:
        node = node.next
        n += 1
    
    if n == 1:
        return True

    i = 0
    node = head
    while i < n//2:
        node = node.next
        i += 1
    
    r_node = reverse(node)
    node.next = None
    node = head
    i = 0
    while i < n//2:
        if r_node.val != node.val:
            return False
        r_node = r_node.next
        node = node.next
        i += 1

    return True