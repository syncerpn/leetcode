# recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        n = len(A)
        def helper(l, r):
            if r < l:
                return None
            m = (l + r) // 2
            return TreeNode(A[m], left=helper(l, m-1), right=helper(m+1, r))
        return helper(0, n-1)