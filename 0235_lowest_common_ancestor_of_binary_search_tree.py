# fairly easy because it is a binary search tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        node = root
        while True:
            if node.val > q.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:
                break
        return node