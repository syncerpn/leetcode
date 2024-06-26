# build node list with inorder traversal
# then build the tree from node list by assign root to the mid node
# and recursively build its left and right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(root):
            if not root:
                return []
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

        def build_bst(nodes):
            if len(nodes) == 0:
                return None
            m = len(nodes) // 2
            root = TreeNode(nodes[m], build_bst(nodes[:m]), build_bst(nodes[m+1:]))
            return root

        nodes = inorder_traversal(root)
        return build_bst(nodes)