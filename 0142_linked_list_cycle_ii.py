#1. floyd's tortoise and hare algorithm with identifying cycle head
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solve(head: ListNode) -> ListNode:
    if not head:
        return None

    n = head.next
    if not n:
        return None

    nn = n.next
    if not nn:
        return None

    while nn:
        if n == nn:
            break
        n = n.next
        nn = nn.next
        if not nn:
            return None

        nn = nn.next
        if not nn:
            return None
    
    i = 0
    n = head
    while n != nn:
        n = n.next
        nn = nn.next
        i += 1
    
    return n