# track min/max nodes + max diff
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            vd, vmin, vmax = 0, root.val, root.val
            if root.left or root.right:
                if root.left:
                    ld, lmin, lmax = helper(root.left)
                    vd = max(vd, ld, abs(root.val - lmin), abs(root.val - lmax))
                    vmin, vmax = min(vmin, lmin), max(vmax, lmax)
                if root.right:
                    rd, rmin, rmax = helper(root.right)
                    vd = max(vd, rd, abs(root.val - rmin), abs(root.val - rmax))
                    vmin, vmax = min(vmin, rmin), max(vmax, rmax)
            return vd, vmin, vmax
        result, _, _ = helper(root)
        return result