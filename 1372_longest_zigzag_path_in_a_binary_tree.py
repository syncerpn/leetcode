# recursive dfs dp
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def travel(root, l, r):
            if root:
                ans[0] = max(ans[0], l, r)
                travel(root.left, 0, l+1)
                travel(root.right, r+1, 0)
        
        travel(root, 0, 0)
        return ans[0]