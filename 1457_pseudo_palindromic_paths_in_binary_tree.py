# use helper with bit count
# pseudo palindromic if there is only one odd counted value
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def helper(root, c):
            if not root:
                return 0
            c ^= 1 << (root.val - 1)
            if not root.left and not root.right:
                if c & (c - 1) == 0:
                    ans[0] += 1
            if root.left:
                helper(root.left, c)
            if root.right:
                helper(root.right, c)
        helper(root, 0)
        return ans[0]