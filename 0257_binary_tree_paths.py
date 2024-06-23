# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:        
        if not root.left and not root.right:
            return [f"{root.val}"]

        path = []
        if root.left:
            path += [f"{root.val}->" + i for i in self.binaryTreePaths(root.left)]
        
        if root.right:
            path += [f"{root.val}->" + i for i in self.binaryTreePaths(root.right)]
        
        return path