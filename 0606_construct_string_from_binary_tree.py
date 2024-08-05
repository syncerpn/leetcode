# recursion as usual
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = f"{root.val}"
        if root.right:
            if root.left:
                s += f"({self.tree2str(root.left)})"
            else:
                s += f"()"
            s += f"({self.tree2str(root.right)})"
        elif root.left:
            s += f"({self.tree2str(root.left)})"
        
        return s