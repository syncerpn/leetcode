# helper makes it easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def helper(root):
            s, c, a = root.val, 1, 0
            if not root.left and not root.right:
                return s, c, 1
            if root.left:
                sl, cl, al = helper(root.left)
                s += sl
                c += cl
                a += al
            if root.right:
                sr, cr, ar = helper(root.right)
                s += sr
                c += cr
                a += ar
            return s, c, a + (root.val == s // c)

        s, c, a = helper(root)
        return a