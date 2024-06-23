# traversal with optimized
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0
        if not root:
            return s

        if root.val >= low and root.val <= high:
            s += root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
        if root.val < low:
            s += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            s += self.rangeSumBST(root.left, low, high)

        return s