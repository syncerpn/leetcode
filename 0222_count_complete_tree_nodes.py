# using complete binary tree property to optimize counting
# where, if left depth and right depth are the same, tree has 2^depth - 1
# otherwise, recursive counting
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ld = self.left_depth(root)
        rd = self.right_depth(root)
        if ld == rd:
            return (1 << ld) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def left_depth(self, root):
        h = 0
        while root:
            root = root.left
            h += 1
        return h
    
    def right_depth(self, root):
        h = 0
        while root:
            root = root.right
            h += 1
        return h