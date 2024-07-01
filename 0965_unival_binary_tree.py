# clean solution by walking through all nodes and compare with root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return True
            return node.val == root.val and check(node.left) and check(node.right)

        return check(root)
