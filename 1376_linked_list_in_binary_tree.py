# knew it should be kmp
# but again, i failed to implement it logically
# this is copied from others for reference
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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        s, dp = [head.val], [0]
        i = 0
        h = head.next
        while h:
            while i > 0 and h.val != s[i]:
                i = dp[i-1]
            if h.val == s[i]:
                i += 1
            s.append(h.val)
            dp.append(i)
            h = h.next
        
        def dfs(r, i):
            if not r:
                return False
            while i > 0 and r.val != s[i]:
                i = dp[i-1]
            if r.val == s[i]:
                i += 1
            return i == len(dp) or dfs(r.left, i) or dfs(r.right, i)
        
        return dfs(root, 0)