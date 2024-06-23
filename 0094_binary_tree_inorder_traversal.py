# recursion is trivial? yes, it is
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

# "Recursive solution is trivial, could you do it iteratively?"
# since you asked:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_path = []
        stack = []
        while root or stack:
            #trying going left-most of the root
            while root:
                stack.append(root)
                root = root.left
            #until cannot proceed further, root is now None
            #go back one level, write down the val, go right, and repeat
            root = stack.pop()
            inorder_path.append(root.val)
            root = root.right

        return inorder_path