# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        D = []
        def helper(node):
            l, r = 0, 0
            if node.left:
                l = helper(node.left)
            if node.right:
                r = helper(node.right)
            if l == r and l != -1:
                D.append(l)
                return l + 1
            return -1
        helper(root)
        D.sort(reverse=True)
        return (1 << (D[k-1] + 1)) - 1 if k <= len(D) else -1