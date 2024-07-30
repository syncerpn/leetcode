# recursively prune subtree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return True
            if not root.left and not root.right:
                return root.val == 0
            l = helper(root.left)
            if l: root.left = None
            r = helper(root.right)
            if r: root.right = None
            return l and r and root.val == 0
        if helper(root):
            return None
        return root