# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans = [0]
        def helper(node):
            l, r = -inf, -inf
            if node.left:
                l = helper(node.left)
            
            if node.right:
                r = helper(node.right)
            
            if node.val >= l and node.val >= r:
                ans[0] += 1
            return max(node.val, l, r)
        
        helper(root)
        return ans[0]