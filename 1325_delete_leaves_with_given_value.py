# tree recursion is beautiful
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return True
            if helper(root.left):
                root.left = None
            if helper(root.right):
                root.right = None
            return root.val == target and not root.left and not root.right

        return None if helper(root) else root
