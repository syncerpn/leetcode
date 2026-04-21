# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        f = 0
        s = [root]
        while s:
            p = inf if f else -inf
            s_next = []
            for node in s:
                v = node.val
                if (v % 2 == f) or (f == 1 and v >= p) or (f == 0 and v <= p):
                    return False
                if node.left:
                    s_next.append(node.left)
                if node.right:
                    s_next.append(node.right)
                p = v
            s = s_next
            f = 1 - f
        return True