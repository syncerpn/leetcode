# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        ans = [0]

        def traverse(node, s=None):
            v = node.val
            l, r = 0, 0
            if node.left:
                l = traverse(node.left, s=s)
                if s is not None:
                    ans[0] = max(ans[0], l * (s - l))
            if node.right:
                r = traverse(node.right, s=s)
                if s is not None:
                    ans[0] = max(ans[0], r * (s - r))

            return v + l + r

        s = traverse(root)
        traverse(root, s=s)
        return ans[0] % MOD