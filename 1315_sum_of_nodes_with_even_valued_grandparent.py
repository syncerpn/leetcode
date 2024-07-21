# just a little bit more inconvenience
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        s = 0
        if root.left:
            if root.left.left:
                s += root.left.left.val
            if root.left.right:
                s += root.left.right.val
        if root.right:
            if root.right.left:
                s += root.right.left.val
            if root.right.right:
                s += root.right.right.val
        if root.val % 2 == 0:
            return s + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
        return self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)