#memoi + recursive traversal should be ok
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0
        def traversal(root):
            nonlocal total_tilt
            if not root:
                return 0
            
            v_left = traversal(root.left)
            v_right = traversal(root.right)
            total_tilt += abs(v_left - v_right)

            return root.val + v_left + v_right
        
        if not root:
            return 0
        
        traversal(root)
        
        return total_tilt