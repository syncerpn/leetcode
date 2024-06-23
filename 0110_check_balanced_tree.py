# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            if not root:
                return 0
            return 1 + max(get_height(root.left), get_height(root.right))
        
        if not root:
            return True
        
        if not self.isBalanced(root.left):
            return False
        
        if not self.isBalanced(root.right):
            return False

        return abs(get_height(root.left) - get_height(root.right)) <= 1