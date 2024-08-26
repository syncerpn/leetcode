# fast and slow mechanic
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        if not fast:
            return None
        while fast:
            fast = fast.next
            if not fast: # even
                slow.next = slow.next.next
                break
            fast = fast.next
            if not fast: # even
                slow.next = slow.next.next
                break
            slow = slow.next
        return head