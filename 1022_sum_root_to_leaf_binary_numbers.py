# accumulate on the way
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        
        s = 0
        if root.left:
            root.left.val += root.val << 1
            s += self.sumRootToLeaf(root.left)
        if root.right:
            root.right.val += root.val << 1
            s += self.sumRootToLeaf(root.right)
        return s
        