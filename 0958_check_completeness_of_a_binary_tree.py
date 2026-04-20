# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        p = True
        s = [root]
        while s and p:
            s_next = []
            for node in s:
                if not node.left:
                    if node.right:
                        return False
                    p = False
                else:
                    if not p:
                        return False
                    s_next.append(node.left)
                    if node.right:
                        s_next.append(node.right)
                    else:
                        p = False
            s = s_next
        return not any([si.left or si.right for si in s])