# recursion as usual
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root):
            ans = [root.val]
            if not root.left and not root.right:
                return ans
            
            gc = []
            if root.left:
                gc += helper(root.left)
            if root.right:
                gc += helper(root.right)
            return ans + [n for n in gc if n >= root.val]
        
        return len(helper(root))