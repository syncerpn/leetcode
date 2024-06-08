#1. create a dummy node to deal with removing head
#2. save two nodes for reference, they should be away from each other by a distance of n+1
#3. keep travelling until one reaches the last node
#4. the other should now be the prev node of the target node
#5. simple assign its next node to the next of the target node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode, n: int):
    dummy = ListNode(0, next=head)
    prev_to_target_node = dummy
    last_node = dummy

    for _ in range(n+1):
        last_node = last_node.next
    
    while last_node is not None:
        last_node = last_node.next
        prev_to_target_node = prev_to_target_node.next
    
    prev_to_target_node.next = prev_to_target_node.next.next

    return dummy.next
