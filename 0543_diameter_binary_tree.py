# check diameter of subtree as well as left-root-right diameter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def scan(root):
            nonlocal diameter
            if not root:
                return -1
            d_left = 1 + scan(root.left)
            d_right = 1 + scan(root.right)
            diameter = max(diameter, d_left + d_right)
            return max(d_left, d_right)
        
        scan(root)
        return diameter