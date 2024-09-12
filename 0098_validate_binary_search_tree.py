# try to bound left and right of any node
# out of bound results in invalid bst
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, l, r):
            if l is not None and l >= root.val:
                return False
            if r is not None and r <= root.val:
                return False
            if root.left:
                if not helper(root.left, l, root.val):
                    return False
            if root.right:
                if not helper(root.right, root.val, r):
                    return False
            return True
        
        return helper(root, None, None)