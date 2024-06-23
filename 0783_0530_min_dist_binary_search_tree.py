# apply to binary search tree, so just traversal inorder and calculate pairwise difference
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(root):
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []
        
        node_vals = inorder_traversal(root)
        d_min = None
        for a, b in pairwise(node_vals):
            if d_min is None or d_min > b-a:
                d_min = b-a
        return d_min
        