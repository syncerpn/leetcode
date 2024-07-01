# recursively plug inc tree left -> root -> inc tree right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root
        
        root_new = root
        l = root.left
        r = root.right
        if l:
            l = self.increasingBST(l)
            root.left = None
            root_new = l
            while l.right:
                l = l.right
            l.right = root

        if r:
            r = self.increasingBST(r)
            root.right = r

        return root_new