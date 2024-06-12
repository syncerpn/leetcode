#1. floyd's tortoise and hare algorithm
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solve(head: ListNode) -> bool:
    if not head:
        return False

    t = head.next
    if not t:
        return False

    h = t.next
    if not h:
        return False
    
    while h:
        if t == h:
            return True
        t = t.next
        h = h.next
        if not h:
            return False
        h = h.next
    
    return False