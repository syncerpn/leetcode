# easy with order
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        r = 0
        d = {}
        node = head
        while node:
            d[node.val] = r
            r += 1
            node = node.next
        nums.sort(key=lambda a: d[a])
        ans = 1
        for a, b in pairwise(nums):
            if d[b] - d[a] > 1:
                ans += 1
        return ans

# or set
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        node = head
        ans = 0
        while node:
            if node.val in s and (node.next is None or node.next.val not in s):
                ans += 1
            node = node.next
        return ans