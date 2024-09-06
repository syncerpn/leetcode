# hash set for quick lookup
# then other things are trivial
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        new_head = ListNode(0, head)
        prev, curr = new_head, head
        while curr:
            if curr.val not in nums:
                prev.next = curr
                prev = curr
            curr = curr.next
        
        prev.next = None

        return new_head.next