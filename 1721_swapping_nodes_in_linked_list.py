# 2-pass trivial
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        node = head
        node_k = None
        while node:
            n += 1
            if n == k:
                node_k = node
            node = node.next
        
        j = n + 1 - k
        n = 0
        node = head
        node_j = None
        while node:
            n += 1
            if n == j:
                node_j = node
                break
            node = node.next
        
        node_j.val, node_k.val = node_k.val, node_j.val
        return head

# 1-pass
# find kth node first
# then use two pointer, going from head and the node found previously until one of them reach null
# then swap
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = head
        for i in range(k-1):
            a = a.next
        
        null = a.next
        b = head
        while null:
            null = null.next
            b = b.next
        
        a.val, b.val = b.val, a.val
        return head