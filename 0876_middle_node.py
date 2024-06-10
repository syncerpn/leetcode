#1. its about space or time
#2. this one sacrifice space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    ref = []
    while head:
        ref.append(head)
        head = head.next
    
    return ref[len(ref)//2]