#1. keep tracking of odd or even by index i, then take turn appending node to even and odd list
#2. at the end, appending None to even list and even list to odd list tail
#3. inplace, so return head
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: ListNode) -> ListNode:
    if not head:
        return None
    if not head.next:
        return head

    i = 3
    odd = head
    even_head = head.next

    even = even_head
    node = head.next.next

    while node:
        if i % 2 == 0:
            even.next = node
            even = node
        else:
            odd.next = node
            odd = node

        node = node.next
        i += 1
    
    even.next = None
    odd.next = even_head
    
    return head
