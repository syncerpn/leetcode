# find the deepest leaves
# then gradually going up to the common ancestor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = [root, 0]
        def helper(root, d):
            if not root:
                return d-1
            
            dl = helper(root.left, d+1)
            dr = helper(root.right, d+1)
            if dl == dr:
                if dl >= ans[1]:
                    ans[1] = dl
                    ans[0] = root
            return max(dl, dr)
        helper(root, 0)
        return ans[0]