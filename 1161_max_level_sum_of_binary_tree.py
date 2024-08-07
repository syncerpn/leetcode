# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 1
        m = None
        s = [root]
        i = 0
        while s:
            i += 1
            t = 0
            s_next = []
            for n in s:
                t += n.val
                if n.left:
                    s_next.append(n.left)
                if n.right:
                    s_next.append(n.right)
            if m is None or m < t:
                m = t
                ans = i
            s = s_next
        return ans