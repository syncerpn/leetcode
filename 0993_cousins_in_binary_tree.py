# bfs, to track parent id of each target node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        s = [root]
        px = None
        py = None
        while s:
            s_next = []
            for i, n in enumerate(s):
                if n.left:
                    s_next.append(n.left)
                    if n.left.val == x:
                        px = i
                    elif n.left.val == y:
                        py = i
                if n.right:
                    s_next.append(n.right)
                    if n.right.val == x:
                        px = i
                    elif n.right.val == y:
                        py = i
            s = s_next

            if px is not None and py is not None:
                return px != py
            if px is None and py is not None:
                return False
            if px is not None and py is None:
                return False
        
        return False