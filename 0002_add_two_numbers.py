#1. simple add-carry logic
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    a1 = l1
    a2 = l2
    c = 0
    a = None
    r = a
    while (a1 is not None) or (a2 is not None):
        if a is None:
            a = ListNode()
            r = a
        else:
            a.next = ListNode()
            a = a.next
        
        if a1 is not None and a2 is not None:
            a.val = (a1.val + a2.val + c) % 10
            c = (a1.val + a2.val + c) // 10
            a1 = a1.next
            a2 = a2.next
        elif a1 is not None:
            a.val = (a1.val + c) % 10
            c = (a1.val + c) // 10
            a1 = a1.next
        elif a2 is not None:
            a.val = (a2.val + c) % 10
            c = (a2.val + c) // 10
            a2 = a2.next

    if c > 0:
        a.next = ListNode()
        a = a.next
        a.val = c
    
    return r