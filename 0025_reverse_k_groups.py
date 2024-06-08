#1. similar to pair swapping, recursion should work
#2. using O(K) space actually if optimized
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    ref = []
    i = 0
    node = head
    while node and i < k:
        ref.append(node)
        node = node.next
        i += 1
    
    if i < k:
        return head

    next_head = ref[i-1].next
    while i > 1:
        ref[i-1].next = ref[i-2]
        i -= 1
    
    ref[0].next = reverseKGroup(next_head, k)

    return ref[k-1]